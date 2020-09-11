from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_movie, get_movie_by_id, search_movie
from .forms import ReviewForm
from ..models.movie import Movie_Review

@main.route('/')
def index():
    ''' Home page
        This view renders the homepage
    '''
    popular_movies = get_movie('popular')
    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('.search', title= search_movie))
    return render_template('index.html',popular_movies = popular_movies)

@main.route('/movie/<int:movie_id>/')
def movie_details(movie_id):
    '''Movie Details
        This view returns single movie details
    '''
    search_movie = request.args.get('movie_query')
    movie = get_movie_by_id(movie_id)
    if search_movie:
        return redirect(url_for('.search', title= search_movie))
    return render_template('single_movie.html', movie=movie)

@main.route('/search/<title>/')
def search(title):
    query = ' '.join(title.split())
    search_results = search_movie(query)
    title = f'Search results for {query}'
    search_movies = request.args.get('movie_query')
    if search_movies:
        return redirect(url_for('.search', title= search_movies))
    return render_template('search.html', search_results = search_results, query=query )

@main.route('/movie/review/new/<int:id>/', methods = ['GET', 'POST'])
def add_review(id):
    form = ReviewForm()
    movie = get_movie_by_id(id)
    if form.validate_on_submit():
        title =form.title.data
        review = form.review.data
        new_review = Movie_Review(movie.id, title, movie.poster, review)
        new_review.save_review()
        return redirect(url_for('movie_details', movie_id= movie.id))
    title = f'{movie.title} review'
    return render_template('add_review.html', title = title, form = form, movie = movie)

@main.route('/movie/review/<int:id>/')
def movie_reviews(id):
    movie = get_movie_by_id(id)
    reviews = Movie_Review.get_reviews(movie.id)
    return render_template('movie_reviews.html', reviews = reviews)



