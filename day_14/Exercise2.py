#Exercise 2

#1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def uppercase(str):
    return str.upper()
upper_countries = map(uppercase, countries)
print(list(upper_countries)) #1

#2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square(x):
    return x ** 2
squared = map(square, numbers)
print(list(squared)) #2

#3
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
upper_names = map(uppercase, names)
print(list(upper_names)) #3

#4
def contains_land(str):
    if 'land' in str:
        return True
    return False
land_countries = filter(contains_land, countries)
print(list(land_countries)) #4

#5
def contains_six(str):
    if 6 == len(str):
        return True
    return False
six_char = filter(contains_six, countries)
print(list(six_char)) #5

#6
def contains_six_or_more(str):
    if len(str) >= 6:
        return True
    return False
more = filter(contains_six_or_more, countries)
print(list(more)) #6

#7
def filter_e(str):
    if 'E' in str:
        return True
    return False
more = filter(filter_e, countries)
print(list(more)) #7

#8
result = map(uppercase, filter(filter_e, countries))
print(list(result))
print(list(result)) #8

#9
variety = ['Warframe', 1999, 'AX-52', 'Mag', 'Nyx']
def get_string_lists(value):
    if isinstance(value, str):
        return True
    return False
only_str = filter(get_string_lists, variety)
print(list(only_str)) #9

#10 Using the previous numbers list
from functools import reduce
def sum_of_two(x, y):
    return x + y
sum = reduce(sum_of_two, numbers)
print(sum) #10

#11
def concat(str, curr):
    if countries.index(curr) == len(countries) - 1:
        return str + ', and ' + curr
    else:
        return str + ', ' + curr
sentence = reduce(concat, countries) + ' are north European countries'
print(sentence) #11

#12
def catagorize_countries(str):
    if 'land' in str:
        return True
    return False
countries_sorted = filter(catagorize_countries, countries)
print(list(countries_sorted)) #12

#13
from countries import countries1
def starting_letters(lst = None):
    if lst == None:
        lst = []
        return 'There are no items to sort.'
    starting_dict = {}
    for country in lst:
        if country[0] in starting_dict:
            starting_dict[country[0]] += 1
        else:
            starting_dict[country[0]] = 1
    return starting_dict
print(starting_letters(countries1))
#14
def first_ten(countries1):
    return countries1[:10]
print(first_ten(countries1)) #14

#15
def last_ten(countries1):
    return countries1[-10:]
print(last_ten(countries1)) #15
