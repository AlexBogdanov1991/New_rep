class TaskQueue:
    def __init__(self):
        self.tasks = []


    def add_task(self, task):
        self.tasks.append(task)

    def get_next_task(self):
        if self.is_empty():
            return None
        return self.tasks.pop(0)

    def is_empty(self):
        return len(self.tasks) == 0


class Task:
    def __init__(self, name):
        self.name = name

queue = TaskQueue()

task1 = Task("Задача 1")
task2 = Task("Задача 2")
task3 = Task("Задача 3")

queue.add_task(task1)
queue.add_task(task2)
queue.add_task(task3)

next_task = queue.get_next_task()
print(f"Следующая задача: {next_task.name if next_task else 'Нет задач'}")  # Ожидаемый результат: "Задача 1"

queue.get_next_task()  # Извлечь следующую задачу

print(f"Очередь пуста: {queue.is_empty()}")