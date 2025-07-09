#Exercise 1

#1/2
dog = {'name':'Joe', 'color':'black', 'legs':'long', 'age': 3}

#3
student_dictionary = {'first_name':'Benjamin', 
                      'last_name':'Chong', 
                      'gender':'male',
                      'age':'20', 
                      'marital_status':'unmarried',
                      'skills':['Java, Python'],
                      'country':'USA',
                      'city':'Sacramento',
                      'address':'(Insert Address)'}
#4
print(len(student_dictionary))

#5
print(student_dictionary['skills'])
print(type(student_dictionary['skills']))

#6
student_dictionary['skills'] = ['Java', 'Python', '100 WPM']
print(student_dictionary['skills'])

#7
print(student_dictionary.keys())

#8
print(student_dictionary.values())

#9
print(student_dictionary.items())

#10
student_dictionary.popitem()
print(student_dictionary)

#11
del student_dictionary