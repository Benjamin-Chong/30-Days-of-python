#Exercise 1

#1 Reading Lines Of A Text
obama = open('obama_speech.txt', 'r')
obama_lines = obama.readlines()
lines = len(obama_lines)
print(f'There are {lines} lines in Obama\'s speech.')
obama.close()

#1a Reading Words From A Text
obama = open('obama_speech.txt', 'r')
obama_text = obama.read()
words = obama_text.split()
print(f'There are {len(words)} words in Obama\'s speech.')
obama.close()

#Michelle_Obama
michelle = open('michelle_obama_speech.txt', 'r')
michelle_lines = michelle.readlines()
print(f'There are {len(michelle_lines)} line in Michelle\'s speech.')
michelle.close()

michelle = open('michelle_obama_speech.txt', 'r')
michelle_words = michelle.read()
words = michelle_words.split()
print(f'There are {len(michelle_words)} words in Michelle\'s speech.')
michelle.close()

#Donald Speech
donald = open('donald_speech.txt', 'r')
donald_lines = donald.readlines()
print(f'There are {len(donald_lines)} lines in Donald\'s speech.')
donald.close()

donald = open('donald_speech.txt', 'r')
donald_words = donald.read()
words = donald_words.split()
print(f'There are {len(words)} words in Donald\'s speech.')
donald.close()

#Melina Trump
melina = open('melina_trump_speech.txt')
melina_lines = melina.readlines()
lines = len(melina_lines)
print(f'There are {lines} lines in Melina\'s speech.')
melina.close()

melina = open('melina_trump_speech.txt')
melina_words = melina.read()
words = melina_words.split()
print(f'There are {len(words)} words in Melina\'s speech.')
melina.close()

#2 Top 10 Most Spoken Languages
import json
file = open('countries_data.json', 'r', encoding = 'utf-8')
countries = json.load(file)
count = {}
for country in countries:
    for lang in country['languages']:
        if lang in count:
            count[lang] += 1
        else:
            count[lang] = 1
sort_10 = sorted(count.items(), key = lambda x:x[1], reverse = True)
print(sort_10[:10])
file.close()

#3 Ten Most Populated Countries
pops = {}
with open('countries_data.json') as f:
    for country in countries:
        pops[country['name']] = country['population']
    sort_pop = sorted(pops.items(), key = lambda x : x[1], reverse = True)
    print(sort_pop[:10])