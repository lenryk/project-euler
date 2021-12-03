import datetime

start = datetime.date(1901, 1, 1)
test = datetime.date(1901, 1, 5)
END = datetime.date(2000, 12, 31)
WEEK_DAYS=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

print(END - start)

leap_years = list()

for year in range(1901, 2001):
  if (year % 4 == 0):
    leap_years.append(year)

print(leap_years)


new_date = start + datetime.timedelta(days=7)
print(new_date)

print(start.weekday())
print(start)

while start.date() is not 1901-1-5:
  start += datetime.timedelta(days=1)
print(start)



  