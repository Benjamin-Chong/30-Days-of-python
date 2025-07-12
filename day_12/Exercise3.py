#Exercise 3

#1
import random
def shuffle(lst = None):
    if lst == None:
        lst = []
    new_lst = lst.copy()
    random.shuffle(new_lst)
    return new_lst

#2
def seven_num():
    seven = []
    while len(seven) < 7:
        gen_number = random.randint(0,9)
        if gen_number in seven:
            gen_number = random.randint(0,9)
        else:
            seven.append(gen_number)
    return seven

#Example Usage
items = ['microphone', 'camera', 'pencil', 'phone', 'keyboard', 'wallet', 'airpods']
print(shuffle(items))
print(seven_num())