# Exercise 1: Print current date and time in Python

import datetime

print(datetime.datetime.now())
# only time
print(datetime.datetime.now().time())

# Exercise 2: Convert string into a datetime object

from datetime import datetime, timedelta

date_string = "Feb 25 2020  4:20PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)

# Exercise 3: Subtract a week (7 days)  from a given date in Python

given_date = datetime(2020, 2, 25)
print("Given date")
print(given_date)

days_to_subtract = 7
res_date = given_date - timedelta(days=days_to_subtract)
print("New Date")
print(res_date)

# Exercise 4: Print a date in a the following format

given_date = datetime(2020, 2, 25)
print("Given date is")
print(given_date.strftime('%A %d %B %Y'))

# Exercise 5: Find the day of the week of a given date

given_date = datetime(2020, 7, 26)

# to get weekday as integer
print(given_date.today().weekday())

# To get the english name of the weekday
print(given_date.strftime('%A'))

# Exercise 7: Print current time in milliseconds

import time

milliseconds = int(round(time.time() * 1000))
print(milliseconds)

# Exercise 10: Calculate number of days between two given dates

date_1 = datetime(2020, 2, 25).date()
date_2 = datetime(2020, 9, 17).date()

delta = None
if date_1 > date_2:
    print("date_1 is greater")
    delta = date_1 - date_2
else:
    print("date_2 is greater")
    delta = date_2 - date_1
print("Difference is", delta.days, "days")
print(type(delta))
