from flask import Flask, render_template, redirect, request
import model 

app = Flask(__name__)

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)

if __name__=="__main__":
    app.run(debug=True)


@app.route("/new_user")
def create_user():
    n_user = User(email= , password=       , age=      , zipcode=      )

    return render_template("new_user.hmtl", )

    session.add(n_user)
    session.commit()




# # @app.route("/login")
# def user_login():

# @app.route("/view_users")
# def view_users():

# @app.route("/ratings_user")
# def view_ratings_user():

# @add.route("/modify_rating")
# def modify_rating():
