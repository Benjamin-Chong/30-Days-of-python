#Exercise 1
#1
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

import re
from collections import Counter
paragraph = paragraph.lower()
words = re.findall(r'\b\w+\b', paragraph, re.I)
word_count = Counter(words)
print(word_count)
most_common = word_count.most_common(1)[0]
print(f'The most common word is {most_common[0]} with a count of {most_common[1]}.')

#2
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
conv_int = list(map(int, points))
sorted_ints = sorted(conv_int)
distance = sorted_ints[-1] - sorted_ints[0]
print(f'The distance between the two extremes is {distance}.')