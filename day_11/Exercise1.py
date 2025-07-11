#Exercise 1

#1
def add_two_numbers(a, b):
    total = a + b
    return total

#2
def area_of_circle(r):
    area = 3.14 * (r ** 2)
    return area

#3
def add_all_nums(number):
    total = 0
    if isinstance(number, int) == True:
         for num in range(number + 1):
            total = total + num
    else:
        print('Not a number.')
    return total

#4
def convert_celsius_to_fahrenheit(cel):
    return (cel * 9/5) + 32

#5
def check_season(month):
    autumn = ['September', 'October', 'November']
    summer = ['June', 'July', 'August']
    spring = ['March', 'April', 'May']
    winter = ['December', 'January', 'February']
    if month in autumn:
        return f'Your month {month} is in autumn'
    elif month in summer:
        return f'Your month {month} is in summer'
    elif month in spring:
        return f'Your month {month} is in spring'
    elif month in winter:
        return f'Your month {month} is in winter'
    else:
        return 'Invalid month.'

#6
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

#7
def solve_quadratic_eqn(a,b,c):
    discriminant = (b ** 2 - 4 * a * c) **0.5
    if discriminant >= 0:
        x1 = (-b + discriminant) / (2 * a)
        x2 = (-b - discriminant) / (2 * a)
        return x1, x2 
    else:
        return 'None exist.'
    
#8
def print_list(lst = []):
    for item in lst:
        print(item, end = ' ')
    print()

#9
def reverse_list(lst = []):
    n = len(lst)
    for item in range(len(lst) // 2):
        temp = lst[item]
        lst[item] = lst[n - 1 - item]
        lst[n - 1 - item] = temp
    return lst

#10
def capilalize_list_items(lst = []):
    for item in range(len(lst)):
        lst[item] = lst[item].capitalize()
    return lst

#11
def add_item(str, lst = []):
    lst.append(str)
    return lst

#12
def remove_item(str, lst =[]):
    if str in lst:
        if len(lst) == 0:
            print('There are no items in the list.')
        elif len(lst) == 1:
            lst.remove(str)
            print('You have deleted the last item in the list.')
        else:
            lst.remove(str)
    else:
        print('Item was not found in the list.')
    return lst

#13
def sum_of_numbers(number):
    total = 0
    for num in range(number + 1):
        total = num + total
    return total

#14
def sum_of_odds(number):
    total = 0
    for num in range(number + 1):
        if num % 2 != 0:
            total = num + total
    return total

#15
def sum_of_evens(number):
    total = 0
    for num in range(number +1):
        if num % 2 == 0:
            total = num + total
    return total

#Example Usage
print(add_two_numbers(1, 5)) #1
print(area_of_circle(1)) #2
print(add_all_nums(3)) #3
print(convert_celsius_to_fahrenheit(28)) #4
print(check_season('March')) #5
print(calculate_slope(2,2, 1,1)) #6
print(solve_quadratic_eqn(1,5,3)) #7
items = ['basket','football', 'keyboard', 'comb'] #8
print_list(items) #8
print(reverse_list(items)) #9
print(capilalize_list_items(items)) #10
print(add_item('airpods', items)) #11
print(remove_item('micky', items)) #12
print(sum_of_numbers(3)) #13
print(sum_of_odds(100)) #14
print(sum_of_evens(100)) #15