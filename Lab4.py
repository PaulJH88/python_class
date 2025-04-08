#Lab4.py

import datetime, calendar

current_date_time = datetime.datetime.now()

birth_date_time = datetime.datetime(1988, 10, 25)

weekday_born = birth_date_time.strftime("%A")

print("Born on a", weekday_born)

print("I am", datetime.datetime.timestamp(current_date_time) - datetime.datetime.timestamp(birth_date_time), "seconds old")

print(calendar.month(1988, 10))
