#Quotes to Scrape

import json
from bs4 import BeautifulSoup
import requests
url = 'https://quotes.toscrape.com/'
response = requests.get(url)
status = response.status_code

text = response.content
parsed = BeautifulSoup(text, 'html.parser')
print(parsed.title.get_text())

quotes = parsed.find_all('div', class_ = 'quote')
data = []

for quote in quotes:
    text = quote.find('span', class_ = 'text').get_text(strip = True)
    author = quote.find('small', class_ = 'author').get_text(strip = True)
    tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]
    data.append({'text': text, 'author': author, 'tags': tags})

with open('quotes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print(f'Scraped {len(data)} quotes from page 1.')