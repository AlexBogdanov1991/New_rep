import json
import csv

# Задание 0
with open('student_list.json', 'r') as file:
    students = json.load(file)


# Задание 1: Средний балл по всем предметам
def get_average_score(students):
    for student in students:
        average_score = sum(student['grades'].values()) / len(student['grades'])
        print(f"Средний балл для студента {student['name']}: {average_score}")


# Задание 2: Наилучший и худший студент
def get_best_student(students):
    best_student = max(students, key=lambda student: sum(student['grades'].values()) / len(student['grades']))
    average_score = sum(best_student['grades'].values()) / len(best_student['grades'])
    print(f"Наилучший студент: {best_student['name']} (Средний балл: {average_score:.2f})")


def get_worst_student(students):
    worst_student = min(students, key=lambda student: sum(student['grades'].values()) / len(student['grades']))
    average_score = sum(worst_student['grades'].values()) / len(worst_student['grades'])
    print(f"Худший студент: {worst_student['name']} (Средний балл: {average_score:.2f})")


# Задание 3: Поиск по имени
def find_student(name):
    student = next((s for s in students if s['name'] == name), None)
    if student:
        print(
            f"Имя: {student['name']}\nВозраст: {student['age']}\nПредметы: {student['subjects']}\nОценки: {student['grades']}")
    else:
        print("Студент с таким именем не найден")


# Задание 4: Сортировка студентов
def sort_students_by_average(students):
    students_sorted = sorted(students, key=lambda student: sum(student['grades'].values()) / len(student['grades']),
                             reverse=True)
    print("Сортировка студентов по среднему баллу:")
    for student in students_sorted:
        average_score = sum(student['grades'].values()) / len(student['grades'])
        print(f"{student['name']}: {average_score:.2f}")


# Задание 5: Преобразование словаря в список
# Это уже сделано в рамках задания 0, так как json загружается в список словарей

# Задание 6: Сохранение в CSV
def save_to_csv(students):
    with open('students.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "age", "average_grade"])

        for student in students:
            average_grade = sum(student['grades'].values()) / len(student['grades'])
            writer.writerow([student['name'], student['age'], average_grade])


# Вызов функций
get_average_score(students)
get_best_student(students)
get_worst_student(students)
find_student("John")
find_student("Emma")
sort_students_by_average(students)
save_to_csv(students)
