class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})"

students_dict = {
    'Саша': 27,
    'Кирилл': 52,
    'Маша': 14,
    'Петя': 36,
    'Оля': 43,
}

students_list = [Student(name, age) for name, age in students_dict.items()]
sorted_students = sorted(students_list, key=lambda x: x.age)
print(sorted_students)


data = [
    (82, 191),
    (68, 174),
    (90, 189),
    (73, 179),
    (76, 184)
]

def calculate_bmi(weight, height):
    height_in_m = height / 100
    return weight / (height_in_m ** 2)

bmi_list = [(calculate_bmi(weight, height), weight, height) for weight, height in data]
sorted_bmi = sorted(bmi_list, key=lambda x: x[0])

for bmi, weight, height in sorted_bmi:
    print(f"Вес: {weight} кг, Рост: {height} см, ИМТ: {bmi:.2f}")


students_list = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36,
    },
    {
        "name": "Оля",
        "age": 43,
    },
]

youngest_student = min(students_list, key=lambda student: student["age"])
print(f"Самый младший ученик: {youngest_student['name']}, возраст: {youngest_student['age']}")
