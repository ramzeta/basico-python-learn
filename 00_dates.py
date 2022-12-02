from datetime import datetime

now = datetime.now()

print(now.hour)
print(now.minute)
print(now.second)
print(now.year)


timestamp = now.timestamp()

print(timestamp)


year_2023 = datetime(2023,1,1)

print(year_2023)


from datetime import time

current_time = time(23,13,22)

print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


from datetime import date

current_date = date(2022,1,1)

print(current_date)
print(current_date.weekday())
print(current_date.today())
print(current_date.timetuple())
print(current_date.year)
print(current_date.month)
print(current_date.day)

