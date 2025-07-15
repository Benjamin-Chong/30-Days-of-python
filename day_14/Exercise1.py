#Exercise 1

#1
#A map is a function that takes in a funciton and its iterable as parameters and is useful for changing a list by a certain value
#A filter returns a boolean for each item of the list that satisfies the criteria as true or false.
#reduce is a function that once again takes two parameters and returns a single value rather than another iterable. Moves from left to right iterating over the iterable using the function given in the first parameter

#2
#A higher order function takes in another a parameter that is then changed via another function and returned.
#A closure is a nesting another function inside of another function where you then return the inner function.
#A decorator takes in a funciton and "enhances" the funcitonality of the "old" function. Denoted by a @decorator before the function is defined.

#3
#Map
numbers = [1, 2, 3, 4, 5, 6]
def square(x):
    return x ** 2

new_list = map(square, numbers)
print(list(new_list))

#Filter
def is_even(x):
    if x % 2 == 0:
        return True
    return False

new_numbers = filter(is_even, numbers)
print(list(new_numbers))

#Reduce
from functools import reduce 
def add(x, y):
    return x + y

reduced = reduce(add, numbers)
print(reduced)

#4
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country, end = ' ')
print()

#5
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name, end = ' ')
print()

#6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num, end = ' ')
print()