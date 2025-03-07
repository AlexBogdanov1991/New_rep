import json


with open('student_list.json', 'r', encoding='utf-8') as file:
    students = json.load(file)


def get_average_score(students):
    average_scores = {}

    for student in students:
        name = student['name']
        grades = student['grades']
        average_score = sum(grades.values()) / len(grades) if grades else 0
        average_scores[name] = average_score
        print(f"Средний балл для студента {name}: {average_score}")

    return average_scores

def get_best_student(average_scores):
    best_student = max(average_scores, key=average_scores.get)
    print(f"Наилучший студент: {best_student} (Средний балл: {average_scores[best_student]:.2f})")

def get_worst_student(average_scores):
    worst_student = min(average_scores, key=average_scores.get)
    print(f"Худший студент: {worst_student} (Средний балл: {average_scores[worst_student]:.2f})")
