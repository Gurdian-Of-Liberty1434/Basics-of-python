from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("Today's date is", today)
print("Current time is", now)

print("\nDate components:", today.day, today.month, today.year)