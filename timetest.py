#!/usr/bin/python

import pytz
from pytz import timezone
from datetime import datetime


fmt = '%Y-%m-%d %H:%M:%S %Z%z'

utc = datetime.now(timezone('UTC'))
print(utc)
oslo = utc.astimezone(timezone('Europe/Oslo'))
print(oslo)
print(oslo.strftime(fmt))



utc_now = datetime.utcnow()
oslo = timezone('Europe/Oslo')
oslo_time = oslo.localize(utc_now)
print(oslo_time)
print(oslo_time.strftime(fmt))


