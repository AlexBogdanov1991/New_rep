fruits = ["apple", "kiwi", "banana", "fig"]
filtered_fruits = list(filter(lambda x: len(x) > 4, fruits))
print(filtered_fruits)

students = [{"name": "John", "grade": 90}, {"name": "Jane", "grade": 85}, {"name": "Dave", "grade": 92}]
top_student = max(students, key=lambda student: student["grade"])
print(top_student)


tuples = [(1, 5), (3, 2), (2, 8), (4, 3)]
sorted_tuples = sorted(tuples, key=lambda x: sum(x))
print(sorted_tuples)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})"


person = [
    Person("John", 24),
    Person("Jane", 19),
    Person("Dave", 22)
]
sorted_person = sorted(person, key=lambda x: x.age)
print(sorted_person)