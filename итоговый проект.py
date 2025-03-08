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
            print(f"Имя: {student['name']}")
            print(f"Возраст: {student['age']}")
            print(f"Предметы: {student['subjects']}")
            print(f"Оценки: {student['grades']}")
            return
    print("Студент с таким именем не найден")


def sort_students_by_average_score():
    average_scores = get_average_score(students)
    sorted_students = sorted(average_scores.items(), key=lambda item: item[1], reverse=True)
    print("Сортировка студентов по среднему баллу:")
    for name, score in sorted_students:
        print(f"{name}: {score:.2f}")


def generate_csv():
    with open('students_average_scores.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'age', 'average_grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        average_scores = get_average_score(students)
        for student in students:
            name = student['name']
            age = student['age']
            average_grade = average_scores[name]
            writer.writerow({'name': name, 'age': age, 'average_grade': average_grade})


average_scores = get_average_score(students)
print("Средние баллы студентов:")
for name, score in average_scores.items():
    print(f"{name}: {score:.2f}")

best_student, best_score = get_best_student(students)
print(f"Наилучший студент: {best_student} (Средний балл: {best_score:.2f})")

worst_student, worst_score = get_worst_student(students)
print(f"Худший студент: {worst_student} (Средний балл: {worst_score:.2f})")

find_student("John")
sort_students_by_average_score()
generate_csv()


