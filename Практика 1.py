
import json

with open('students.json', 'r', encoding='utf-8') as file:
    students = json.load(file)

total_students = len(students)
print(f"Общее количество студентов: {total_students}")

oldest_student = None
for student in students:
    if oldest_student is None or student['возраст'] > oldest_student['возраст']:
        oldest_student = student

print(f"Студент с самым высоким возрастом:\nИмя: {oldest_student['имя']}, Возраст: {oldest_student['возраст']}, Город: {oldest_student['город']}")

python_students_count = 0
for student in students:
    if "Python" in student['предметы']:
        python_students_count += 1

print(f"Количество студентов, изучающих Python: {python_students_count}")
