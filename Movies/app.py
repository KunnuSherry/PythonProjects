from flask import Flask, render_template, request, redirect, url_for, jsonify, json
import requests

app=Flask(__name__)


def movieByName(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key=dfa7df7d1299efae7358ef1c992610c0&query={title}"
    response = requests.get(url)
    data = response.json()
    if(data["results"]):
        title = data["results"][0]["original_title"]
        temp_url = data["results"][0]["poster_path"]
        image = f"https://image.tmdb.org/t/p/w500{temp_url}"
        desc = data["results"][0]["overview"]
        ratings = data["results"][0]["vote_average"]

    return title, image, desc, ratings

def getGenres():
    url = "https://api.themoviedb.org/3/genre/movie/list?api_key=dfa7df7d1299efae7358ef1c992610c0"
    response = requests.get(url)
    data = response.json()
    genres={}
    for genre in data["genres"]:
        genres[genre["name"].lower()] = genre["id"]
    return genres

def moviesByGenres(genre):
    genre_map = getGenres()
    print(genre_map)
    id = genre_map.get(genre)
    print(id)
    url = f"https://api.themoviedb.org/3/discover/movie?api_key=dfa7df7d1299efae7358ef1c992610c0&with_genres={id}"
    response = requests.get(url)
    data = response.json()

    titles = []
    images = []
    desc = []
    ratings = []
    if data.get("results"):
        for i in range(0, min(5, len(data["results"]))):  # Ensure we don't exceed available results
            titles.append(data["results"][i]["original_title"])
            temp_url = data["results"][i]["poster_path"]
            images.append(f"https://image.tmdb.org/t/p/w500{temp_url}")
            desc.append(data["results"][i]["overview"])
            ratings.append(data["results"][i]["vote_average"])
    
    return titles, images, desc, ratings

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/movie', methods=['POST', 'GET'])
def movie():
    if request.method=='POST':
        t = request.form.get('title').lower()
        title, image, desc, ratings = movieByName(t)
    return render_template('movieDetails.html', title=title, image=image, desc=desc, ratings=ratings)

@app.route('/movies', methods=['POST', 'GET'])
def movies():
    if(request.method=='POST'):
        tag = request.form.get('tag')
        titles, images, desc, ratings = moviesByGenres(tag)
        print(titles)
        
    return render_template('movies.html', titles=titles, images=images, desc=desc, ratings=ratings)

if __name__=="__main__":
    app.run(debug=True)