#Exercise 1

#1 For loop
for i in range(11):
    print(i)

#while loop
i = 0
while i <= 10:
    print(i)
    i = i + 1

#2 for loop
for i in range(10, 0, -1):
    print(i)

#while loop
i = 10
while i >= 0:
    print(i)
    i = i - 1

#3
for i in range(1,7):
    for j in range(i):
        print('#', end = '')
    print()

#4
for i in range(1,8):
    for j in range(1,8):
        print('#', end = ' ')
    print()

#5
for i in range(11):
    print(f'{i} x {i} = {i*i}')

#6
lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for i in lst:
    print(i, end = ' ')
print()

#7
for i in range (101):
    if i % 2 == 0:
        print(i, end = ' ')
print()

#8
for i in range (101):
    if i % 2 != 0:
        print(i, end = ' ')
print()