#Day 6

#1 Tuples cannot be changed and are ordered
empty_tuple = ()
print(empty_tuple)

#2
names = ('Ava','Chase', 'Ella')
print(names)

#3
brothers = ('Chase', )
sisters = ('Ava', 'Ella')
siblings = brothers + sisters
print(siblings)

#4
print(len(siblings))

#5
parents = ('Tham', 'Eric')
family_members = siblings + parents
print(family_members)