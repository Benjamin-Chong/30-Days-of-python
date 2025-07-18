#Exercise 3
import re
from collections import Counter
sentence = '%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'
cleaned = re.sub(r'[^\w\s]', '', sentence).lower()
print(cleaned)

word_counter = re.findall(r'\b\w+\b', cleaned, re.I )
word  = Counter(word_counter)
top_five = word.most_common(3)
print(top_five)