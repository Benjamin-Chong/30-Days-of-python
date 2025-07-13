#Exercise

#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero = [i for i in numbers if i <= 0]

#2
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
combined = [number for row in list_of_lists for number in row]


#3
lst = [(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)] 
result = [(i, i**0, i**1, i**2, i**3, i**4, i**5, i**6) for i in range(11)]

#4
countries = [('Finland', 'Helsinki'), ('Sweden', 'Stockholm'), ('Norway', 'Oslo')]
upper_list = [(country.upper(), country[0:3].upper(), capital.upper()) for country, capital in countries ]

#5
countries = [('Finland', 'Helsinki'), ('Sweden', 'Stockholm'), ('Norway', 'Oslo')]
new_list = [{'country': country.upper(), 'city': city.upper()} for [country, city] in countries]


#6
names = [('Asabeneh', 'Yetayeh'), ('David', 'Smith'), ('Donald', 'Trump'), ('Bill', 'Gates')]
lst = [f'{first_name + ' ' + last_name}' for first_name, last_name in names]


#7
def slope(x1, y1, x2, y2):
    if x1 == x2:
        return 'Invalid: vertical line'
    m = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
    return 'Slope: ' + f'{m(x1, y1, x2, y2)}'



def b(x1, y1, m):
    b = y1 - m * x1
    return f'y-intercept: {b}'

#Example Usage:
print(negative_zero) #1
print(combined) #2
print(result) #3
print(upper_list) #4
print(new_list) #5
print(lst) #6
print(slope(1, 1, 2, 2)) #7
print(b(1,1,1)) #7