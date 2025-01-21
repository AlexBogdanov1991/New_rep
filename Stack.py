class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0


def is_valid_parenthesis_sequence(sequence):
    stack = Stack()
    opening = {'(': ')', '{': '}', '[': ']'}

    for char in sequence:
        if char in opening.keys():
            stack.push(char)
        elif char in opening.values():
            if stack.is_empty() or opening[stack.pop()] != char:
                return False
    return stack.is_empty()



input_sequence = input("Введите скобочную последовательность: ")


if is_valid_parenthesis_sequence(input_sequence):
    print("Правильная скобочная последовательность.")
else:
    print("Неправильная скобочная последовательность.")

