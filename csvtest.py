user = session.query(Users).get(35)
ratings = session.query(Ratings).filter_by(user_id=user.id).all()
movies = []
for r in ratings:
	movie = session.query(Movie).get(r.movie_id)
	movies.append(movie)

for m in movies:
	print m.title