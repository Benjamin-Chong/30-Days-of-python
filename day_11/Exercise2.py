#Exercise 2

#1
def evens_and_odds(number):
    total_even = 0
    total_odd = 0
    for num in range(number + 1):
        if num % 2 == 0:
            total_even += 1
        else:
            total_odd += 1
    return {'Evens', total_even, 'Odds', total_odd}

#2
def factorial(number):
    if number == 0:
        return 1
    result = 1
    for num in range(number, 1, -1):
        result = result * num
    return result

#3
def is_empty(item):
    if item:
        print('Exists and not empty.')
    else:
        print('Value is empty or none.')

#4
def calculate_mean(lst = None):
    total = 0
    if lst == None:
        lst = []
    for num in range(len(lst)):
        total = total + lst[num]
    total = total / len(lst)
    return total

def calculate_median(lst = None):
    if lst == None:
        lst = []
    lst.sort()
    mid = len(lst) // 2
    if len(lst) % 2 != 0:
        median = lst[mid]
        return median
    else:
        mid_1 = lst[mid]
        mid_2 = lst[mid - 1]
        median = (mid_1 + mid_2) / 2
        return median

def calculate_mode(lst = None):
    if lst == None:
        lst = []
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    sorted_count = sorted(count.items(), key = lambda x : x[1], reverse = True)
    return sorted_count[0][0]
    
def calculate_range(lst = None):
    if lst == None:
        lst = []
    lst.sort()
    range = lst[len(lst) - 1] - lst[0]
    return range

def calculate_variance(lst = None):
    if lst == None:
        lst = []
    mean = calculate_mean(lst)
    for num in range(len(lst)):
        lst[num] = (lst[num] - mean) ** 2

    total = 0
    for num in lst:
        total = total + num
    return total / len(lst)

def calculate_std(lst = None):
    if lst == None:
        lst = []
    var = calculate_variance(lst)
    return var ** 0.5

#Example Usage:
print(evens_and_odds(100)) #1
print(factorial(4)) #2
is_empty('') #3
numbers = [0, 5, 15, 59, 11] #4
print(calculate_mean(numbers)) #4
print(calculate_median(numbers)) #4
print(f'Mode value: {calculate_mode(numbers)}') #4
print(calculate_range(numbers))
print(calculate_variance(numbers))
print(calculate_std(numbers))