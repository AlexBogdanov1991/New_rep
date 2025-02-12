
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

