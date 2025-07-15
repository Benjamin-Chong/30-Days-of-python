#Exercise 3

#1
from countries_data import data
def sort_name(lst = None):
    if lst == None:
        lst = []
        return 'There are no items in the list'
    return sorted(lst, key = lambda x: x['name'])

def sort_pop(lst = None):
    if lst == None:
        lst = []
        return 'There are no items in the list'
    return sorted(lst, key = lambda x: x['population'], reverse = True)

def sort_capital(lst = None):
    if lst == None:
        lst = []
        return 'There are no items in the list'
    return sorted(lst, key = lambda x: x['capital'])

def top_lang(lst = None):
    if lst == None:
        lst = []
        return 'There are no items in the list'
    spoken_lang = {}
    for country in lst:
        for lang in country['languages']:
            if lang in spoken_lang:
                spoken_lang[lang] += 1
            else:
                spoken_lang[lang] = 1
    return [(lang, count) for lang, count in sorted(spoken_lang.items(), key=lambda x: x[1], reverse=True)][:10]


#Example Usage:
print(sort_name(data))
print(sort_pop(data))
print(top_lang(data))
print(sort_pop(data)[:10])


