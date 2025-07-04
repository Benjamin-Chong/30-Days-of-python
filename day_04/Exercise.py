#Exercise Day 4

#1
first = 'Thirty '
second = 'Days '
third = 'Of '
fourth = 'Python'
full = first + second + third + fourth
print(full)

#2
first = 'Coding '
second = 'For '
third = 'All'
full = first + second + third
print(full)

#3
company = 'Coding For All'

#4
print(company)

#5
print(len(company))

#6
print(company.upper())

#7
print(company.lower())

#8
string = 'Coding For All'
print(string.capitalize())
string = 'Coding For All'
print(string.title()) #no change here because it is already in the title format
string = 'Coding For All'
print(string.swapcase())

#9
string = 'Coding For All'
for_all = company[-7:] #indexes from the last character in the string
print(for_all)

#10
string = 'Coding For All'
print(string.find('Coding'))

#11
string = 'Python For All'

#12
print(string.replace('All', 'Everyone')) #order here seems to not matter

#13
string = 'Coding For All'
print(string.split())

#14
string = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(string.split(', '))

#15
string ='Coding For All'
print(string[0])

#16
string = 'Coding For All'
print(string[-1])

#17
string = 'Coding For All'
print(string[10])

#18
string = 'Python For Everyone'
acr = 'PFE'

#19
string = 'Coding For All'
acr = 'CFA'

#20
string = 'Coding For All'
print(string.index('C'))

#21
string = 'Coding For All'
print(string.index('F'))

#22
string = 'Coding For All'
print(string.rindex('l')) #case matters

#23
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

#24
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

#25
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace('because ', ''))

#26 was already done in 23 basically the same problem

#27 already done in 24

#28
string = 'Coding For All'
print(string.startswith('Coding'))

#29
string = 'Coding For All'
print(string.endswith('coding'))

#30
string = ' Coding For All '
print(string[1:-1]) #removes the first and the last space

#31
string = '30DaysOfPython'
string2 = 'thirty_days_of_python'
print(string.isidentifier()) #checks if the first value is a number. if number = false
print(string2.isidentifier())

#32
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(list))

#33
two_sentences = 'I am enjoying this challenge. \nI just wonder what is next.'
print(two_sentences)

#34
str = 'Name \t\t Age \t Country \t City \nBenjamin \t 20 \t   USA \t      Sacramento'
print(str)

#35
rad = 10
area = 3.14 * rad ** 2
print('The area of a circle with radius {} is {} meters squared.'.format(rad, area))

#36
a = 8
b = 6
print(8 / 6)
print('%d + %d = %d' %(a, b, a + b)) #using the old style
print('{} - {} = {}'.format(a,b, a - b)) #using the new style 
print(f'{a} * {b} = {a * b}') #using string interpolation
print('%d / %d = %f' %(a, b, a / b)) #using the old style
print('{} % {} = {}'.format(a,b, a % b)) #using the new style 
print(f'{a} // {b} = {a // b}') #using string interpolation
print('%d ** %d = %d' %(a, b, a ** b)) #using the old style

