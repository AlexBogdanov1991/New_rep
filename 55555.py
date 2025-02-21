import itertools

items = [1, 2, 3, 4]
for c in itertools.combinations(items, 2):
    print(c)


import itertools

items = ['P', 'y', 't', 'o', 'n']
for p in itertools.permutations(items):
    print(p)


import itertools

list1 = ['a', 'b']
list2 = [1, 2, 3]
list3 = ['x', 'y']

combined_list = list1 + list2 + list3
cycle_iterator = itertools.cycle(combined_list)
result = [next(cycle_iterator) for _ in range(len(combined_list) * 5)]

print(result)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()
first_10_fibs = [next(fib_gen) for _ in range(10)]

print(first_10_fibs)



import itertools

list5 =  ['red', 'blue']
list6 = ['shirt', 'shoes']
combinations = itertools.product(list5,list6)
for combination in combinations:
    print(' '.join(combination))