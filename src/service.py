import boto3


def export_log_group(log_group_name: str, start_time: int, end_time: int):
    client = boto3.client('logs')

    # Prepare required parameters
    request_params = {
        "logGroupName": log_group_name,
        "startTime": start_time,
        "endTime": end_time,
        # "limit": 10000
    }

    iteration_number = 1
    response = client.filter_log_events(**request_params)

    log_events = response.get("events", [])
    print(f"Round {iteration_number} / {len(log_events)} events")

    blob_content = ""
    for log_event in log_events:
        blob_content += log_event.get("message") + "\n"

    while response.get("nextToken"):
        iteration_number += 1
        request_params["nextToken"] = response.get("nextToken")
        response = client.filter_log_events(**request_params)
        log_events = response.get("events", [])
        print(f"Round {iteration_number} / {len(log_events)} events")
        for log_event in log_events:
            blob_content += log_event.get("message").rstrip() + "\n"

        # TODO: Limit to 10 MB

    # TODO: Use smart open to stream to S3

    # Write to S3 Object
    # s3_bucket_name = "cl-cedric01-logs-647217338613"
    # s3_object_key = f"logs/exported/manual/cl-cedric01-ecs/ecs/container/cm01-gcr-dev/{operation_id}.log"

    # s3_object_uri = f"s3://{s3_bucket_name}/{s3_object_key}"
    # upload_log_content_to_s3(ctx=ctx, bucket_name=s3_bucket_name, object_key=s3_object_key, content=blob_content)
    # print(f"Log Exported to {s3_object_uri}")

    # Return the S3 Object Signed URL
    # return s3_object_uri
    return blob_content
