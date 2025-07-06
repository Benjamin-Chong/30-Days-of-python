#Day 6

#1
family_members = ('Chase', 'Ava', 'Ella', 'Tham', 'Eric')
x, y, z, a, b = family_members
print(x)
print(b)

#2
fruits = ('apples', ) #must add the comma to indicate a tuple if not it will be read as a string
vegetables = ('lettuce', )
animal_products = ('wagyu', )
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#4
removed_items = food_stuff_tp[1:2]
print(removed_items)

#5
fruits = ('apples', 'oranges' ) #must add the comma to indicate a tuple if not it will be read as a string
vegetables = ('lettuce', )
animal_products = ('wagyu', 'pork skin', 'pork blood')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
sliced_first = food_stuff_lt[0:3]
print(sliced_first)
sliced_last = food_stuff_lt[2:5]
print(sliced_last)

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)