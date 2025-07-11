#Exercise 3

#1
def is_prime(number):
    if number < 2:
        return False
    else:
        for num in range(2, int(number ** 0.5) + 1):
            if number % num == 0:
                return False
    return True
            
#2
def is_unique(lst = None):
    if lst == None:
        lst = []
        return 'List is empty'
    return len(lst) == len(set(lst))

#3
def all_same_data_type(lst = None):
    if lst == None:
        lst = []
    first_type = type(lst[0])
    for item in range(len(lst)):
        if first_type != type(lst[item]):
            return False
    return True

#4
def python_var(variable):
    return variable.isidentifier()

#5
def most_spoken_languages(lst = None):
    if lst == None:
        lst = []
    lang_count = {}
    for country in lst:
        for language in country['languages']:
                lang_count[language] = lang_count.get(language, 0) + 1
    sorted_lang = sorted(lang_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_lang[:10]

#6
def most_populated_countries(lst = None):
    if lst == None:
        lst = []
    pop_dict = {}
    for country in lst:
        pop_dict[country['name']] = country['population']
    sorted_pop = sorted(pop_dict.items(), key = lambda x:x[1], reverse = True)
    return sorted_pop[:10]


#Example Usage
    print(is_prime(2))
items = ['Stars', 'Masks', 'Mirrors', 1]
print(is_unique(items))
print(all_same_data_type(items))
print(python_var('x'))
import json
with open('day_11/countries_data.json', 'r', encoding = 'utf-8') as file:
    data = json.load(file)
print(most_spoken_languages(data))
print(most_populated_countries(data))