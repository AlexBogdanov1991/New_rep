
import json

with open('students.json', 'r', encoding='utf-8') as file:
    students = json.load(file)

total_students = len(students)
print(f"Общее количество студентов: {total_students}")

oldest_student = None
for student in students:
    if oldest_student is None or student['возраст'] > oldest_student['возраст']:
        oldest_student = student

print(f"Студент с самым высоким возрастом:\n")
print(f"Имя: {oldest_student['имя']}")
print(f"Возраст: {oldest_student['возраст']}")
print(f"Город: {oldest_student['город']}")

python_students_count = 0
for student in students:
    if "Python" in student['предметы']:
        python_students_count += 1

print(f"Количество студентов, изучающих Python: {python_students_count}")




import csv
from collections import defaultdict
from datetime import datetime

sales_data = []
with open('sales.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        sales_data.append({
            'date': datetime.strptime(row['Дата'], '%Y-%m-%d'),
            'product': row['Продукт'],
            'amount': float(row['Сумма'])
        })

total_sales = sum(sale['amount'] for sale in sales_data)
print(f'Общая сумма продаж: {total_sales}')

product_sales = defaultdict(float)
for sale in sales_data:
    product_sales[sale['product']] += sale['amount']

best_product = max(product_sales, key=product_sales.get)
print(f'Продукт с самым высоким объемом продаж: {best_product} (Сумма: {product_sales[best_product]})')

monthly_sales = defaultdict(float)
for sale in sales_data:
    month_year = sale['date'].strftime('%Y-%m')
    monthly_sales[month_year] += sale['amount']

print('Общая сумма продаж по месяцам:')
for month, total in monthly_sales.items():
    print(f'{month}: {total}')







with open('employees.json', 'r', encoding='utf-8') as json_file:
    employees = json.load(json_file)

performance = {}
with open('performance.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        employee_id = row['employee_id']
        score = float(row['performance_score'])
        performance[employee_id] = score

for employee in employees:
    employee_id = employee['id']
    if employee_id in performance:
        employee['performance_score'] = performance[employee_id]

total_performance = 0
highest_performance = 0
best_employee = None
employee_count = 0

for employee in employees:
    if 'performance_score' in employee:
        total_performance += employee['performance_score']
        employee_count += 1
        if employee['performance_score'] > highest_performance:
            highest_performance = employee['performance_score']
            best_employee = employee['name']

if employee_count > 0:
    average_performance = total_performance / employee_count
    print(f"Средняя производительность: {average_performance:.2f}")
    if best_employee:
        print(f"Сотрудник с наивысшей производительностью: {best_employee} ({highest_performance:.2f})")
else:
    print("Нет данных о производительности.")
