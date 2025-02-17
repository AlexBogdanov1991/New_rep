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


from datetime import datetime

user_input = input("Введите дату в формате 'год-месяц-день' (например, '2023-12-31'): ")
target_date = datetime.strptime(user_input, '%Y-%m-%d')

current_date = datetime.now()
time_difference = target_date - current_date
days_remaining = time_difference.days
hours_remaining, seconds = divmod(time_difference.seconds, 3600)
minutes_remaining, _ = divmod(seconds, 60)

print(f"Осталось: {days_remaining} дней, {hours_remaining} часов и {minutes_remaining} минут.")
