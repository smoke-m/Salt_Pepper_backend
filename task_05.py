from datetime import datetime, timedelta

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def date_in_future(integer):
    """
    Вернет дату через integer дней.
    """
    if type(integer) is not int:
        return datetime.now().strftime(DATE_FORMAT)
    return (datetime.now() + timedelta(days=integer)).strftime(DATE_FORMAT)
