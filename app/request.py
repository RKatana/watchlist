import os
import requests
# import urllib.request,json 
from .models.movie import Movie

api_key = None
base_url = None
search_url = None

def configure_request(app):
    global api_key, base_url, search_url
    api_key = os.environ.get('MDB_API_KEY')
    base_url = app.config.get('MDB_BASE_URL')
    search_url = app.config.get('MDB_SEARCH_URL')

def get_movie(category):
    get_movies_url = base_url.format(category,api_key)
    movie_result = None
    with requests.get(get_movies_url) as response:
        data = response.json()

        if data['results']:
            movies_list = data.get('results')
            movie_results = process_results(movies_list)
    return movie_results

def process_results(movies_list):
    movie_results =[]
    for movie in movies_list:
        id = movie.get('id')
        title = movie.get('title')
        overview = movie.get('overview')
        poster = movie.get('poster_path')
        # thumbnail = movie.get('backdrop_path')
        vote_average = movie.get('vote_average')
        vote_count = movie.get('vote_count')
        release_date = movie.get('release_date')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count, release_date)
            movie_results.append(movie_object)
        
    return movie_results

def get_movie_by_id(id):
    url = base_url.format(id, api_key)
    movie = None
    with requests.get(url) as response:
        data = response.json()
        if data:
            id = data.get('id')
            title = data.get('original_title')
            overview = data.get('overview')
            poster = data.get('poster_path')
            # thumbnail = data.get('backdrop_path')
            vote_average = data.get('vote_average')
            vote_count = data.get('vote_count')
            release_date = data.get('release_date')
            movie = Movie(id,title,overview,poster,vote_average,vote_count, release_date)

    return movie

def search_movie(query):
    url = search_url.format(api_key, query)
    with requests.get(url) as response:
        data = response.json()
        search_results = None
        if data['results']:
            search_response = data.get('results')
            search_results = process_results(search_response)
    return search_results