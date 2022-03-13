import json
from datetime import datetime, timezone
from typing import Dict

from cerberus import Validator
from dateutil.parser import isoparse

from commons import datetime_utils
from exceptions import ValidationError
from service import export_log_group


def get_operation_params_from_sqs_message(sqs_message: Dict):
    sqs_records = sqs_message.get("Records", [])
    if not sqs_records:
        return
    event_body = sqs_records[0].get("body", "")
    return json.loads(event_body)


def make_datetime_utc_timezone_aware(dt: datetime):
    if not dt.tzinfo:
        return dt.replace(tzinfo=timezone.utc)


def lambda_handler(event, context):
    print(f"EVENT: {json.dumps(event)}")
    print(f"CONTEXT: {context}")

    operation_params = get_operation_params_from_sqs_message(sqs_message=event)
    if operation_params is None:
        return
    else:
        print(f"Parameters: {json.dumps(operation_params)}")

    # Prepare default date values (UTC / timezone aware / ISO 8601 format)
    date_now_iso8601 = make_datetime_utc_timezone_aware(datetime.utcnow()).isoformat()
    date_one_month_ago_iso8601 = make_datetime_utc_timezone_aware(
        datetime_utils.get_datetime_one_month_ago(reset_clock=True)).isoformat()

    # Event Validation
    schema = \
        {'logGroupName': {'type': 'string'},
         'fromTime':
             {'type': 'string',
              'default': date_one_month_ago_iso8601},
         'toTime':
             {'type': 'string',
              'default': date_now_iso8601},
         }
    validator = Validator(schema)
    normalized_params = validator.normalized(operation_params)

    # TODO Write a function that better handle validation errors output
    if not validator.validate(normalized_params):
        print("Validation Error")
        return "Validation Error"

    from_time_dt = isoparse(normalized_params.get("fromTime"))
    to_time_dt = isoparse(normalized_params.get("toTime"))

    # Finally, check that starting date is older than ending date
    if not datetime_utils.is_before(from_time_dt, to_time_dt):
        from_time_str = normalized_params.get("fromTime")
        to_time_str = normalized_params.get("toTime")
        error_msg = f"Ending date cannot be anterior to starting date (from: {from_time_str}, to: {to_time_str})"
        print(error_msg)
        raise ValidationError(error_msg)

    log_group_name = normalized_params.get("logGroupName")
    from_date_int = int(from_time_dt.timestamp() * 1000)
    to_date_int = int(to_time_dt.timestamp() * 1000)

    log_events = export_log_group(log_group_name=log_group_name, start_time=from_date_int, end_time=to_date_int)
    return log_events
