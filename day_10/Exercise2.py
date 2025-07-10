#Exercise 2

#1
total = 0 
for i in range(101):
    total = total + i
print(f'The sum of all of the numbers is {total}.')

#2
total_even = 0
total_odd = 0
for i in range (101):
    if i % 2 == 0:
        total_even = total_even + i
    else:
        total_odd = total_odd + i
print(f'The sum for all of the evens are {total_even}.')
print(f'The sum for all of the odds are {total_odd}.')
