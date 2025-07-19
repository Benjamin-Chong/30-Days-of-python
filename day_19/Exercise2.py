#Exercise 2

#1
emails = set()
with open('email_exchanges_big.txt') as f:
    for line in f:
        if line.startswith('From '):
            parts = line.split()
            if len(parts) > 1:
                emails.add(parts[1])
    print(emails)

#2
def most_common_words(file, length):
    with open(file) as f:
        txt = f.read()
        words = txt.split()
        count = {}
        for word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
        count_sort = sorted(count.items(), key = lambda x:x[1], reverse = True)[:length]
    return count_sort

#3
print(most_common_words('obama_speech.txt', 2))
print(most_common_words('michelle_obama_speech.txt', 2))
print(most_common_words('donald_speech.txt', 2))
print(most_common_words('melina_trump_speech.txt', 2))

#4
import re
def clean_text(str):
    text = str.lower()
    text = re.sub(r'[.?!,]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def remove_support_words(text):
    from stop_words import stop
    words = text.split()
    filtered_words = [w for w in words if w.lower() not in stop]
    return ' '.join(filtered_words)

def similarity(file1, file2):
    f1 = open(file1, 'r')
    word_str1 = f1.read()
    string1 = clean_text(word_str1)
    string1 = remove_support_words(string1)

    f2 = open(file2, 'r')
    word_str2 = f2.read()
    string2 = clean_text(word_str2)
    string2 = remove_support_words(string2)

    set1 = set(string1.split())
    set2 = set(string2.split())

    intersection = set1.intersection(set2)
    union = set1.union(set2)
    sim = len(intersection) / len(union)

    f1.close()
    f2.close()
    return sim

print(similarity('michelle_obama_speech.txt', 'melina_trump_speech.txt'))

#5
print(most_common_words('romeo_and_juliet.txt', 5))

#6
import re
with open('hacker_news.csv') as hacker:
    lines = hacker.readlines()
    text = ''.join(lines)
    match = re.findall(r'\bpython\b', text, re.I)
    print(len(match))

with open('hacker_news.csv') as hacker:
    lines = hacker.readlines()
    text = ''.join(lines)
    match = re.findall(r'\bjavascript\b', text, re.I)
    print(len(match))

with open('hacker_news.csv') as hacker:
    lines = hacker.readlines()
    text = ''.join(lines)
    java_only_lines = [line for line in lines if re.search(r'\bjava\b', line, re.I) and not re.search(r'\bjavascript\b', line, re.I)]
    print(len(java_only_lines))

