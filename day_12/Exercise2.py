#Exercise 2

#1
import random
def gen_hex(amount):
    hex_colors = []
    character = '0123456789abcdef'
    for _ in range(amount):
        hex_colors.append('#' + ''.join(random.choices(character, k = 6)))
    return hex_colors

#2
def rgb_colors_list(amount):
    rgb_colors = []
    for _ in range(amount):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rgb_colors.append(f'rgb({r}, {g}, {b})')
    return rgb_colors
#3

def gen_colors(format, gen_amount):
    if format == 'hexa':
        character = '0123456789abcdef' #creates a sting of var that random can take from later on
        hexa = ['#' + ''.join(random.choices(character, k = 6)) for i in range(gen_amount)]
        print(hexa)
    elif format == 'rgb':
        rgb_colors = []
        for i in range(gen_amount):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            rgb_colors.append(f'rgb({r}, {g}, {b})')
        print(rgb_colors)
    else:
        return None

#Example Usage
print(gen_hex(2)) #1
print(rgb_colors_list(3)) #2
gen_colors('rgb', 2) #3