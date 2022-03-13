from datetime import datetime

from dateutil.relativedelta import relativedelta


def is_after(date1: datetime, date2: datetime) -> bool:
    """Return True if date1 is more recent than date2.

    Args:
        date1 (datetime): First date to compare
        date2 (datetime): Second date to compare

    Returns:
        True if date1 is posterior to date2. Else False.
    """
    return date1 > date2


def is_before(date1: datetime, date2: datetime) -> bool:
    """Return True if date1 is older than date2.

    Args:
        date1 (datetime): First date to compare
        date2 (datetime): Second date to compare

    Returns:
        True if date1 is anterior to date2. Else False.
    """
    return date1 < date2


def get_datetime_one_month_ago(dt: datetime = datetime.utcnow(), reset_clock: bool = False) -> datetime:
    """ Return the datetime that correspond to the day one month ago.
    Args:
        dt (datetime): The reference date (default: now())
        reset_clock (bool): If True, the clock is reset to 00:00:00, if False the clock is untouched (default: False)

    Returns:
        datetime
    """
    if reset_clock:
        result_datetime = dt + relativedelta(months=-1, hour=0, minute=0, second=0, microsecond=0)
    else:
        result_datetime = dt + relativedelta(months=-1)
    return result_datetime


def get_datetime_one_year_ago(dt: datetime = datetime.utcnow(), reset_clock: bool = False) -> datetime:
    """ Return the datetime that correspond to the day one year ago.
        Args:
            dt (datetime): The reference date (default: now())
            reset_clock (bool): If True, the clock is reset to 00:00:00, if False the clock is untouched (default: False)

        Returns:
            datetime
        """
    if reset_clock:
        result_datetime = dt + relativedelta(years=-1, hour=0, minute=0, second=0, microsecond=0)
    else:
        result_datetime = dt + relativedelta(years=-1)
    return result_datetime
