#UCI DATA

#The links did not work so I decided to practice on my own using my own dataset.

#loading in the data and cleaning
file = open('adult.data')
text = file.readlines()
lines = []
for line in text:
    lines.append(line)

def parts(text):
    fixed = text.strip().split(', ')
    return fixed

#1 How many people with a Bachelor’s make <=50k
amount_of_people = 0
for line in lines:
    if 'Bachelors' in line and '<=50K' in line:
        amount_of_people += 1

#Example Usage for #1
print(f'There are {amount_of_people} who have a Bachelor\'s degree and make less than 50k.')

#2 Average hours worked per week by people who make more than 50k
total_hours = 0
amount_of_persons = 0
for line in lines:
    indexed = parts(line)
    if len(indexed) < 15:
        continue
    if indexed[14] == '>50K':
        total_hours += int(indexed[12])
        amount_of_persons += 1
avg = total_hours / amount_of_persons
#Example Usage for #2
print(f'The average amount of hours worked from people who make more than 50k is {avg} hours.')