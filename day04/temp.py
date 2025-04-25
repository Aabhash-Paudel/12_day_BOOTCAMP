import calendar
from datetime import datetime

year = int(input("year = "))
month = int(input("month= "))
day = int(input("day= "))

date = datetime.now()
currYear = date.year
currMonth = date.month
currday = date.day

total = 0

for y in range(year, currYear):
    if calendar.isleap(y):
        total += 366
    else:
        total += 365
