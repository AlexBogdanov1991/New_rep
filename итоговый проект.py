
import json
import csv

with open('student_list.json', 'r', encoding='utf-8') as file:
    students = json.load(file)

def get_average_score(students):
    average_scores = {}
    for student in students:
        name = student['name']
        grades = student['grades']
        average_score = sum(grades.values()) / len(grades) if grades else 0
        average_scores[name] = average_score
        student['average_score'] = average_score
    return average_scores

def get_best_student(students):
    average_scores = get_average_score(students)
    best_student = max(average_scores, key=average_scores.get)
    return best_student, average_scores[best_student]

def get_worst_student(students):
    average_scores = get_average_score(students)
    worst_student = min(average_scores, key=average_scores.get)
    return worst_student, average_scores[worst_student]

def find_student(name):
    for student in students:
        if student['name'].lower() == name.lower():
            return student
    return None

def sort_students_by_average_score():
    average_scores = get_average_score(students)
    sorted_students = sorted(students, key=lambda student: student['average_score'], reverse=True)
    return sorted_students

def generate_csv():
    with open('students_average_scores.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'age', 'average_score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow({'name': student['name'], 'age': student['age'], 'average_score': student['average_score']})

average_scores = get_average_score(students)
print("Средние баллы студентов:")
for student in students:
    print(f"{student['name']}: {student['average_score']:.2f}")

best_student, best_score = get_best_student(students)
print(f"Наилучший студент: {best_student} (Средний балл: {best_score:.2f})")

worst_student, worst_score = get_worst_student(students)
print(f"Худший студент: {worst_student} (Средний балл: {worst_score:.2f})")

student = find_student("John")
if student:
    print(f"Имя: {student['name']}")
    print(f"Возраст: {student['age']}")
    print(f"Предметы: {student['subjects']}")
    print(f"Оценки: {student['grades']}")
    print(f"Средний балл: {student['average_score']:.2f}")
else:
    print("Студент с таким именем не найден")

sorted_students = sort_students_by_average_score()
print("Сортировка студентов по среднему баллу:")
for student in sorted_students:
    print(f"{student['name']}: {student['average_score']:.2f}")

generate_csv()
