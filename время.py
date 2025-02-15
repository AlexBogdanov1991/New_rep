
import datetime

now = datetime.datetime.now()

print(f"Текущая дата и время: {now}")

day_of_week = now.strftime("%A")
print(f"День недели: {day_of_week}")

year = now.year
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap_year:
    print(f"Год {year} является високосным.")
else:
    print(f"Год {year} не является високосным.")

