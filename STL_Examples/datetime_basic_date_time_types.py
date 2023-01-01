# The datetime module supplies classes for manipulating dates and times

from datetime import timedelta
delta = timedelta(days=10,
                  weeks=2,
                  hours=9,
                  minutes=5)
print(delta)

from datetime import date, datetime

d = date(2022,12,31)
print(d.replace(day=12))
print(date(2022,12,31).isoformat())
print(date(2022,12,31).ctime())
print(date.today().isoformat())
print(datetime.now().isoformat())
print(datetime.now())

dt = datetime.now()
tt = dt.timetuple()
for it in tt:
    print(it)

ic = dt.isocalendar()
for it in ic:
    print(it)


