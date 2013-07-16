from model import Rating, User, Movies, connect
from datetime import datetime

import csv


def load_users(session):
    # use u.user
    with open('seed_data/u.user', 'rb') as csvfile:
        f = csv.reader(csvfile, delimiter = "|")
        for row in f:
            user = User(age=row[1], zipcode=row[4])
            session.add(user)
        session.commit()

def load_movies(session):
    # use u.item
    with open('seed_data/u.item', 'rb') as csvfile:
        f = csv.reader(csvfile, delimiter= "|")
        for row in f:
            dateobject = row[2]
            title = row[3]
            title=title.decode("latin-1")
            dateobject = datetime.strptime("01-Jan-1995", "%d-%b-%Y")
            movie = Movies(name=title, released_at=dateobject, imdb_url=row[4])
            session.add(movie)
        session.commit()

def load_ratings(session):
    with open('seed_data/u.data', 'rb') as csvfile:
        f = csv.reader(csvfile, delimiter = "\t")
        for row in f:
            rating = Rating(movie_id=row[1], user_id=row[0], rating=row[2])
            session.add(rating)
        session.commit()

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_users(session)
    load_movies(session)
    load_ratings(session)
    

if __name__ == "__main__":
    s= connect()
    main(s)
