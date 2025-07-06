#Day 3: Exercise 30 Days of Python Programming

age = 20
height = 166.37
a = 3 + 5j

#Triangle Area Calc
base = int(input('Enter a base for a triangle: '))
height = int(input('Enter a height a triangle: '))
area = 0.5 * base * height
print('The area of the triangle is: ', area)

#Triangle Perimeter Calc
a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
per = a + b + c
print('Perimeter of a the triangle is', per)

#Rectangle Permimeter/Area Calc
length = int(input('Enter a length: '))
width = int(input('Enter a width: '))

per = 2 * (length + width)
area = length * width
print('Permeter of the rectangle: ', per)
print('Area of the rectangle:', area)

#Circle Area/Circumference Calc
rad = int(input('Enter a radius: '))
area = 3.14 * rad * rad
circ = 2 * 3.14 * rad
print('Area of the circle: ', area)
print('Circumferemce of the circle: ', circ)

#Slope Calc
m1 = 2
b = -2 

xint = -b/m1
yint = b
print('Slope of the first: ', m1, '- x intercept: ', xint, '- y int: ', yint)

#Slope Calc and Euclidean Distance
x1, y1 = 2, 2
x2, y2 = 6, 10

m2 = (y2-y1) / (x2 - x1)
dist = ((y2-y1) ** 2 + (x2 - x1) ** 2) ** 0.5
print('Slope of the second:', m2)
print('Distance between both points: ', dist)

#Comparison
if m1 > m2:
    print('Slope 1 is larger')
elif m2 > m1:
    print("Slope 2 is larger")
else:
    print("Both equations have the same slope")

#X Intercept Problem
#Equation: y = x^2 + 6x + 9

a = 1
b = 6
c = 9
disc = b ** 2 - 4 * a * c
if disc >= 0:
    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print('The root(s) where y = 0 are', x1, 'and', x2)
else:
    print('Does not exist')

#Comparing Strings

len1 = len('python')
len2 = len('dragon')

print(len1 != len2)

#And To Compare
str1 = 'python'
str2 = 'dragon'

if 'on' in str1 and 'on' in str2:
    print('On is found in both words')
else:
    print('On is not found in both words')

str3 = 'I hope this course is not full of jargon.'

if 'jargon' in str3:
    print('Jargon is in the string')
else:
    print('Jargon was not found in the string')

#Converting
len1 = float(len1)
print(len1)
len1 = str(len1)
print(len1)

#Remainder
number = int(input('Enter a number: '))
if number % 2 != 0:
    print('This number is odd.')
else:
    print('This number is even.')

#Floor division converted to float
floor = 7 // 3
print(floor)
num = int(2.7)
print(num) #The results were 2 and 2 therefore it is not equalto the value of 2.7.

#Type checking
print(type('10'))
print(type(10)) #False because the first is a string and the second is an int

#Equal 9.8 = 10 after conversion
num = int(9.8) #rounds down
if num == 10:
    print("Equals")
else:
    print('Not equal')

#Calculate the Pay
hrs = int(input('Enter hours: '))
rate = int(input('Enter rate: ')) 
earning = hrs * rate
print('Your weekly earnings are: $', earning)

#Calculate Seconds Lived
years = int(input('Enter the years lived: '))
seconds = years * 365 * 24 * 60 * 60 
print('You have lived for ', seconds, 'seconds.')

#Table
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')
