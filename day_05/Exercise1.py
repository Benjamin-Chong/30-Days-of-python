#Exercise 1

#1
list = list()

#OR

list_alt = []

#2
five_list = ['apples', 'oranges', 'watermelon', 'mangos', 'dragonfruit']

#3
print(len(five_list))

#4
print(five_list[0])
print(five_list[2])
print(five_list[4])

#5
mixed_data_types = ['Benjmain', 20, 5.42, False, '[Insert Address]']

#6 / #7
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(mixed_data_types)
print(it_companies)

#8
print(len(it_companies))

#9
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[6])

#10
it_companies.pop() #last element
print(it_companies)

#11
it_companies.append('Cisco')
print(it_companies)

#12
it_companies.insert(3, 'SAP')
print(it_companies)

#13
it_companies[0] = it_companies[0].upper()
print(it_companies)

#14
new_list = '#'.join(it_companies)
print(new_list)

#15
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies.count('Google'))

#16
it_companies.sort()
print(it_companies)

#17
it_companies.sort(reverse = True)
print(it_companies)

#18
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(0)
it_companies.pop(1)
it_companies.pop(2)
print(it_companies)

#19
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
for i in range(3):
    it_companies.pop()
print(it_companies)

#20
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(3)
print(it_companies)

#21
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(0)
print(it_companies)

#22
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(3)
print(it_companies)

#23
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(6)
print(it_companies)

#24
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
for i in range(7):
    it_companies.pop()
print(it_companies)

#25
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

#27
full_stack = front_end
full_stack.insert(0, 'Python')
full_stack.insert(1,'SQL')
full_stack.insert(2, 'Redux')
print(full_stack)