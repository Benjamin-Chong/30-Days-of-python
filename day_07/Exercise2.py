#Exercise 2

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
A.update(B)
print(A)

#2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
inter =A.intersection(B)
print(inter)

#3 A subset is a set where all the elements in A is contained in B 
sub = A.issubset(B)
print(sub)

#4 Disjoin is when two sets do not share any common elements
disjoint = A.isdisjoint(B)
print(disjoint)

#5
join_AB = A.union(B)
join_BA = B.union(A)
print(join_AB)
print(join_BA)

#6 Only items that are the same in A and B
symmetric_diff = A.symmetric_difference(B)
print(symmetric_diff)

#7
del A
del B
del sub
del disjoint
del symmetric_diff
