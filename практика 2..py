
import random
from collections import Counter

random_list = [random.randint(1, 100) for _ in range(20)]
counter = Counter(random_list)
most_common = counter.most_common(3)

print("Случайный список чисел:", random_list)
print("Три наиболее часто встречающихся элемента:")
for num, count in most_common:
    print(f"Число {num} встречается {count} раз")  #задание 1



from collections import defaultdict

grouped_items = defaultdict(list)

grouped_items['фрукты'].append('яблоко')
grouped_items['фрукты'].append('банан')
grouped_items['овощи'].append('морковь')
grouped_items['фрукты'].append('апельсин')
grouped_items['овощи'].append('картофель')   #Задание 3

for category, items in grouped_items.items():
    print(f"{category}: {items}")


from collections import deque
queue = deque([1, 2, 3, 4, 5, 6, 7,]) #задание 4
queue.append(8)
queue.appendleft(0)
print(queue)

queue.pop()
queue.popleft()
print(queue)


from collections import deque

def append_to_queue(queue, item):
    queue.append(item)

def append_left_to_queue(queue, item):
    queue.appendleft(item)

def pop_from_queue(queue):
    return queue.pop() if queue else None

d = deque([])

append_to_queue(d, 1)
append_left_to_queue(d, 0)
removed_item = pop_from_queue(d)

print(d)
print("Удаленный элемент:", removed_item)
# задание 5






from collections import namedtuple

Book = namedtuple('Book', ['title', 'author', 'genre'])


book1 = Book(title='Мастер и Маргарита', author='Михаил Булгаков', genre='Роман')

books = [book1]

for book in books:
    print(f'Название: {book.title}, Автор: {book.author}, Жанр: {book.genre}')
# задание 2