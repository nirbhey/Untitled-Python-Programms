import datetime
from datetime import date, timedelta

date_from = '2016-02-28'
date_to = '2016-03-02'
d0 = date(int(date_from[:4]), int(date_from[5:7]), int(date_from[8:10]))
d1 = date(int(date_to[:4]), int(date_to[5:7]), int(date_to[8:10]))
list_of_dates = [d0 + timedelta(days=x) for x in range((d1 - d0).days + 1)]

for i in list_of_dates:
    print(i)

print(list_of_dates)
print('Number of dates: ', len(list_of_dates))

date_from = datetime.datetime.now().strftime("%Y%m%d") # Gives today's(System's) date.
print(date_from)