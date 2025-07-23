from flask import Flask, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Open Library Book Search</h1>
        <form action="/search" method="GET">
            <label for="query">Enter book or author:</label>
            <input type="text" id="query" name="q" required>
            <input type="submit" value="Search">
        </form>
    '''

@app.route('/search')
def search():
    query = request.args.get('q')
    search_url = f"https://openlibrary.org/search?q={query}"
    response = requests.get(search_url)
    parsed = BeautifulSoup(response.content, 'html.parser')
    
    results = parsed.find_all('li', class_='searchResultItem')
    
    if not results:
        return f"<h2>No results found for '{query}'</h2>"
    
    books = []
    for item in results[:10]:
        title_tag = item.h3.find('a', class_='results')
        title = title_tag.get_text(strip=True) if title_tag else 'No Title'

        author_tag = None
        for a_tag in item.find_all('a'):
            href = a_tag.get('href', '')
            if href.startswith('/authors/'):
                author_tag = a_tag
                break

        author = author_tag.get_text(strip=True) if author_tag else 'Unknown Author'

        books.append({'title': title, 'author': author})

    html = f"<h2>Search Results for '{query}':</h2><ul>"
    for book in books:
        html += f"<li><strong>{book['title']}</strong> by {book['author']}</li>"
    html += "</ul>"

    return html

if __name__ == '__main__':
    app.run(debug=True)
