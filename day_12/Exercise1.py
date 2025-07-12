#importing a module practice

import mymodule
print(mymodule.generate_full_name('Benjamin', 'Chong'))

#1
import random
import string
def random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k = 6))

#2
def user_id_gen_by_user():
    num_char = int(input('Enter the amount of characters in the randomly generated code: '))
    num_gen = int(input('Enter the amount of codes generated: '))

    characters = string.ascii_letters + string.digits
    for num in range(num_gen):
        print(''.join(random.choices(characters, k = num_char)))

#3
from random import randint
def rgb_color_gen():
    rgb = [randint(0,255) for i in range(3)]
    return f'({rgb[0]}, {rgb[1]}, {rgb[2]})'

#Example Usage:
print(random_user_id())
user_id_gen_by_user()
print(rgb_color_gen())