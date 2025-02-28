def square(x):
    return x ** 3

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(squared)



def is_even(x):
    return x %  5== 0

numbers = [12, 5, 24, 40, 45, 56, 75, 18, 59, 10]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)



from functools import reduce

def is_odd(n):
    return n % 2 != 0

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = filter(is_odd, numbers)
product_of_odds = reduce(multiply, odd_numbers, 1)

print(product_of_odds)