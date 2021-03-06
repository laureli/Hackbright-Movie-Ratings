# here is where we organize our database tables



join on user_id

User:
    id: integer
    age: integer
    gender: string
    zip_code: string (technically zip codes aren't numeric
    email: optional string
    password: optional string

Movie:
    id: integer
    name: string
    released_at: datetime
    imdb_url: string

Rating:
    id: integer
     user_id: integer
    rating: integer

A user has many ratings
A rating belongs to a user
A movie has many ratings
A rating belongs to a movie
A user has many movies through ratings
A movie has many users through ratingsn