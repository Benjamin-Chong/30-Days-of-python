from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', body_class='home')

@app.route('/about')
def about():
    return render_template('about.html', body_class='')
    
@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'GET':
        return render_template('post.html', title='Text Analyzer')
    if request.method == 'POST':
        content = request.form['content']
        word_count = len(content.split())
        char_count = len(content)
        most_common_word = max(set(content.split()), key=content.split().count) if content.strip() else None

        return render_template('result.html',
                               content=content,
                               word_count=word_count,
                               char_count=char_count,
                               most_common_word=most_common_word,
                               title='Result')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
