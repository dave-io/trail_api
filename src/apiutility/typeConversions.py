from django.utils import timezone
from datetime import datetime
import pytz


def toUiReadableDateFormat(value):
    try:
        if value is None:
            return ""

        localizedValue = timezone.localtime(
            value, pytz.timezone('Africa/lagos'))
        return datetime.strftime(localizedValue, "%b %d, %Y %I:%M%p")
    except Exception as ex:
        print(ex)
        return str(value)