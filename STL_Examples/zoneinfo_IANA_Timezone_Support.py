# The zoneinfo module provides a concrete time zone implementation to support the IANA time zone database
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

dt=datetime.today()
print(dt)

# dt = datetime(2022,12,31,tzinfo=ZoneInfo('America/San_Francisco'))
dt = datetime(2022,12,31,tzinfo=ZoneInfo('America/Los_Angeles'))
print(dt)
print(dt.replace(fold=1))
print(dt.tzname())

dt = datetime(2022,12,31,tzinfo=ZoneInfo('Europe/Berlin'))
print(dt)
print(dt.replace(fold=1))
print(dt.tzname())