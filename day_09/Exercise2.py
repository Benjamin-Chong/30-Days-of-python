#Exercise 2

#1
score = float(input('Please enter your score: '))
if score <= 100 and score >= 80:
    print('A')
elif 79 > score and score >= 70:
    print('B')
elif score < 69 and score >= 60:
    print('C')
elif score < 59 and score >= 50:
    print('D')
elif score < 49 and score >= 0:
    print('F')
else:
    print('Enter a valid score.')

#2
month = str(input('Please enter a month. '))
autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
if month in autumn:
    print(f'Your month, {month}, is in autumn.')
elif month in winter:
    print(f'Your month, {month}, is in winter.')
elif month in spring:
    print(f'Your month, {month} is in spring.')
elif month in summer:
    print(f'Your month, {month}, is in summer.')
else:
    print('Enter a valid month.')

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input('Enter a fruit: '))
if fruit in fruits:
    print('This fruit is already in the list.')
else:
    fruits.append(fruit)
    print(fruits)