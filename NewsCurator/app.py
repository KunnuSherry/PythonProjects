from flask import Flask, redirect, render_template, request
import requests

app = Flask(__name__)


def get_top_5_news(keyword):
    url = f'https://newsapi.org/v2/everything?q={keyword}&pageSize=5&apiKey=8cf5dcdbaa734e60ad595dcf3e7f428a'
    response = requests.get(url)
    data = response.json()

    # Arrays to store authors, titles, and descriptions
    authors = []
    titles = []
    descriptions = []

    if data['status'] == 'ok':
        # Extract the top 5 news articles
        top_articles = data['articles']
        for article in top_articles:
            authors.append(article['author'])  # Store the author
            titles.append(article['title'])  # Store the title
            descriptions.append(article['description'])  # Store the description
        return authors, titles, descriptions


@app.route('/', methods=['GET', 'POST'])
def main():
    authors=[]
    titles=[]
    descriptions=[]
    if request.method=='POST':
        keyword = request.form.get('keyword')
        authors, titles, descriptions = get_top_5_news("cricket")
    return render_template('index.html', authors=authors, titles=titles, descriptions=descriptions)

if __name__=="__main__" :
    app.run(debug=True)


