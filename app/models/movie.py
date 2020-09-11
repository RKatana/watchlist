class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count, release_date):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        # self.thumbnail = 'https://image.tmdb.org/t/p/w500/'+ thumbnail
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.release_date = release_date

    def __str__(self):
        return f'{self.title}, votes: {self.average}'

class Movie_Review:
    '''This class defines function to add reviews to single movie item'''
    all_reviews = list()
    def __init__(self, movie_id, movie_title, imageurl, review):
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.imageurl = imageurl
        self.review = review
    
    def save_review(self):
        self.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        cls.all_reviews.clear()

    @classmethod
    def get_reviews(cls, id):
        response = list()
        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)
        return response

    def __str__(self):
        return f'{movie_title} \n {self.review}'

