from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy.orm import sessionmaker, scoped_session

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

# ENGINE = None
# Session = None

# def connect():
#     global ENGINE 
#     global Session
#     return Session()


engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,
                                autocommit=False,
                                autoflush=False))


Base = declarative_base()
Base.query = session.query_property()

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
    movie_id = Column(Integer, ForeignKey('Movies.id'))
    user_id = Column(Integer, ForeignKey('Users.id'))    #table_name.column_name
    rating = Column(Integer)

    user = relationship("User", backref = backref("Ratings", order_by= id))



### End class declarations

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
