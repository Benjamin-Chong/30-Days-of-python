import requests
import json
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/category/books/religion_12/index.html'

response = requests.get(url)
html = response.content
books_religion = BeautifulSoup(html, 'html.parser')

books = books_religion.find_all('article', class_ = 'product_pod')
data = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_ = 'price_color').get_text(strip = True)
    data.append({'title':title, 'price':price})

with open('./day_22/jsons/religious_books.json', 'w', encoding = 'utf-8') as file:
    json.dump(data, file, indent = 4, ensure_ascii = False)

print(f'Scraping has finished. {len(data)} lines of data were scraped and added to the file.')