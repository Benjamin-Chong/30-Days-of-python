#Exercise 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    mid_index = len(person['skills']) // 2
    mid_skills = person['skills'][mid_index]
    print(f'The middle skill is {mid_skills}.')

if 'Python' in person['skills']:
    print(True)
else:
    print(False)

if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a full stack developer.')
elif 'React' in person['skills'] and 'Javascript' in person['skills']:
    print('He is a front end developer.')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a backend developer.')
else:
    print('Unknown title.')

if person['is_married'] == True and 'Finland' in person['country']:
    print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.')