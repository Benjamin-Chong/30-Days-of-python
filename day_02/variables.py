#Day 2: 30 Days of Python Programming (Exercise 1)

first_name = 'Benjamin'
last_name = 'Chong'
country = 'Vietnam'
city= 'Paris'
age = 20
year = 2025
is_married = False
is_light_on = False
is_basic, is_broke, car = True, True, 'Porsche'

#Exercise 2

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(is_basic))
print(type(is_broke))
print(type(car))

firstLength = len(first_name)
lastLength = len(last_name)
if firstLength > lastLength:
    print('First name has more characters.')
elif lastLength > firstLength:
    print('Last name has more characters')
else:
    print('Both names have the same amout of characters')

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

rad = int(input('Enter a valid radius: '))
area_of_circle = 3.14 * (rad ** 2)
circum_of_circle = 2 * 3.14 * rad
print(area_of_circle)
print(circum_of_circle)

first_name = str(input('Enter your first name: '))
last_name = str(input('Enter your last name: '))
country = str(input('Enter your country\'s name: '))