from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy.orm import sessionmaker

ENGINE = None
Session = None

def connect():
	global ENGINE 
	global Session

	ENGINE = create_engine("sqlite:///ratings.db", echo=True)
	Session = sessionmaker(bind=ENGINE)

	return Session()


Base = declarative_base()

### Class declarations go here

class User(Base):

	__tablename__ = "Users"
	id = Column(Integer, primary_key = True)
	email = Column(String(64), nullable= True)
	password = Column(String(64), nullable = True)
	age = Column(Integer, nullable = True)
	zipcode = Column(String(15), nullable = True)

class Movies(Base):

	__tablename__ = "Movies"
	id = Column(Integer, primary_key = True)
	name = Column(String(64)) 
	released_at = Column(DateTime)
	imdb_url = Column(String(64))


class Rating(Base):
	__tablename__ = "Ratings"
	id = Column(Integer, primary_key = True)
	movie_id = Column(Integer)
	user_id = Column(Integer)
	rating = Column(Integer)



### End class declarations

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
