#Exercise 1 

#1 Top 10 Most Frequent Words
import requests
import string
from collections import Counter
url = 'https://www.gutenberg.org/files/1112/1112-0.txt'
data = requests.get(url)
data_split = data.text.split()
text = [word.strip(string.punctuation).lower() for word in data_split]
count = Counter(text)
print(count.most_common(10))


#2 Read Cat API
cat_api = 'https://api.thecatapi.com/v1/breeds'
cat_data = requests.get(cat_api)
cat_data = cat_data.json()
cat_list = []

#get data and sort (weight)
for cat in cat_data:
    cat_list.append(cat['weight']['metric'])
average_weight = []
for weight in cat_list:
    min, max = weight.split(' - ')
    min = int(min)
    max = int(max)
    average = (min + max) / 2
    average_weight.append(average)

sorted_weight = sorted(average_weight, reverse = True)
print(sorted_weight)

#mean
amount = 0
total = 0
for weight in sorted_weight:
    total += weight
    amount += 1
mean = total / amount

#median
middle = len(sorted_weight) // 2 #remainder
if len(sorted_weight) % 2 != 0:
    median = sorted_weight[middle]
else:
    median = (sorted_weight[middle] + sorted_weight[middle - 1]) / 2

#standard deviation
standard_dev = 0
for weight in sorted_weight:
    standard_dev += ((weight - mean) ** 2)
standard_dev = (standard_dev / amount) ** 0.5

#Example Usage for #2
print(f'The min weight of the data is {sorted_weight[0]} and the max weight of the data is {sorted_weight[-1]}.')
print(f'The mean of the data is {mean} in metric units.')
print(f'The median of the data is {median} in metric units.')
print(f'The standard deviation of the data set is {standard_dev}')

#2 Part 2 Years Instead of Weight
years = []
for year in cat_data:
    years.append(year['life_span'])

average_years = []
for year in years:
    min, max = year.split(' - ')
    min = int(min)
    max = int(max)
    average = (min + max) / 2
    average_years.append(average)

sorted_years = sorted(average_years, reverse = True)
min = sorted_years[-1]
max = sorted_years[0]

#mean
amount = 0
total = 0
for year in sorted_years:
    total += year
    amount += 1
mean = total / amount

#median
middle = len(sorted_years) // 2 #remainder
if len(sorted_years) % 2 != 0:
    median = sorted_years[middle]
else:
    median = (sorted_years[middle] + sorted_years[middle - 1]) / 2

#standard deviation
standard_dev = 0
for year in sorted_years:
    standard_dev += ((year - mean) ** 2)
standard_dev = (standard_dev / amount) ** 0.5

#Example Usage for #2 Part 2 
print(f'The min of the years are {min} years and the max of the years are {max} years.')
print(f'The mean years of the data is {mean} in metric units.')
print(f'The median years of the data is {median} in metric units.')
print(f'The standard deviation of the data set is {standard_dev}')

#Frequency Table
from collections import Counter
origin = []
for cat in cat_data:
    origin.append(cat['origin'])

count = Counter(origin)
print(count)

