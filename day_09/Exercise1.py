#Exercise 1

#1

age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to learn how to drive.')
else:
    more_years = 18 - age
    print(f'You need {more_years} more years to learn how to drive.')

#2
my_age = 20
your_age = int(input('Please enter your age: '))
if my_age > your_age:
    print(f'I am older than you by {my_age - your_age} years.')
elif my_age < your_age:
    print(f'You are older than me by {your_age - my_age}.')
else:
    print('We are the same age.')

#3
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
if a > b:
    print(f'{a} is greater than {b}.')
elif b > a:
    print(f'{b} is greater than {a}.')
else:
    print('Both numbers are the same.')
