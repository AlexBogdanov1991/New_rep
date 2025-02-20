class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            raise Exception("Очередь пуста. Нельзя извлечь элемент.")
        return self.items.pop(0)
    def is_empty(self):

        return len(self.items) == 0
    def size(self):
        return len(self.items)
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Размер очереди:", queue.size())
while not queue.is_empty():
    item = queue.dequeue()
    print("Извлечен элемент:", item)


