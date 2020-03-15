#!/usr/bin/python

import pytz
from pytz import timezone
from datetime import datetime


fmt_utc = '%Y-%m-%d %H:%M:%S %Z%z'
fmt = '%Y-%m-%d %H:%M:%S %Z'

utc = datetime.now(timezone('UTC'))
print(utc.strftime(fmt_utc))
oslo = utc.astimezone(timezone("Europe/Oslo"))
print(oslo.strftime(fmt))


naive_now = datetime.now()
oslo_tz = timezone("Europe/Oslo")
oslo_time = oslo_tz.localize(naive_now)
print(oslo_time.strftime(fmt))
oslo_utc = oslo_time.astimezone(timezone('UTC'))
# Should print UTC+0100 ?
print(oslo_utc.strftime(fmt_utc))

