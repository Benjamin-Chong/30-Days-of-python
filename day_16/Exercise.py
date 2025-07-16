#1
from datetime import datetime
currently = datetime.now()
print('Time now:', currently)

#2
formatted = currently.strftime('%m/%d/%Y, %H:%M:%S')
print('Formatted datetime:', formatted)

#3
from datetime import date
december_fifth = datetime.strptime('5 December, 2019', '%d %B, %Y')
print('Parsed date:', december_fifth)

#4
currently = date(2025, 7, 16)
new_year = date(2026, 1, 1)
diff = new_year - currently
print('Days until new year', diff)

#5
from datetime import timedelta
t1 = date(2025, 7, 16)
t2 = date(1970, 1, 1)
print('Days since Jan 1, 1970:', t1 - t2)

#6
#The datetime module is useful for adding the time to a blog post or anything related to posting. Lets say a shopping company is launching their online website. It would be useful to track when the orders were place for order accuracy.