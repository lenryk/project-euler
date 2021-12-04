import datetime

start = datetime.date(1901, 1, 1)
END = datetime.date(2000, 12, 31)

counter = 0
while start != END:
  start += datetime.timedelta(days=1)

  if start.weekday() == 6:
    if start.strftime("%d") == "01":
      counter += 1

print(counter)
