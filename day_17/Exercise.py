#Exercise

#1
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
#unpacking
first_five = names[:5]
print(first_five)
es = names[5]
ru = names[6]
print(es)
print(ru)

#Extra practice to practice the rest of the concepts:

#try / except:
#Try:
try:
    print(5 + 5)
except TypeError:
    print('Error with the types.')

#Except
try:
    print(5 + '5')
except TypeError:
    print('Error with the types.')

#Unpacking
numbers = [ i for i in range(7)]
first, *middle, last = numbers
print(first)
print(numbers)
print(last)

#Packing
def sum_all(*arg):
    sum = 0
    for num in arg:
        sum += num
    return sum
print(sum_all(0, 1, 2, 3, 4, 5))

#Spreading
lst1 = [1, 2]
lst2 = [3, 5, 6, 7, 10]
lst = [0, 0.5, *lst1, *lst2, 100]
print(lst)

#Enumerate
for index, item, in enumerate([10, 20, 30, 40]):
    print(index, item)

#Zip
names = ['Ben', 'Chase']
ages = [20, 12]
names_ages = []
for n, a in zip(names, ages):
    names_ages.append({'name':n, 'age':a})
print(names_ages)