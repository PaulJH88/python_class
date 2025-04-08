import datetime, calendar

date = datetime.datetime(2015, 4, 20)
now = datetime.datetime.now()

print(date, type(date))
print(now)

print(date.strftime("%Y, %B %d, %A"))

timestamp = 1648254827
print(datetime.datetime.fromtimestamp(timestamp))

april = calendar.month(2025, 4)
print(april)