from flask import Flask, render_template, redirect, request
import model 

app = Flask(__name__)

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)


@app.route("/new_user")
def get_user():
    print "wtf people"
    return render_template("new_user.hmtl")


@app.route("/create_user")
def create_user():
    n_user = User(email= request.form.get("email"), 
                    password=request.form.get("password"),
                    age=request.form.get("age"), 
                    zipcode=request.form.get("zipcode"))
    
    session.add(n_user)
    session.commit()


@app.route("/punch_user")
def punch_face():

    return "hit you in the face"



# # @app.route("/login")
# def user_login():

# @app.route("/view_users")
# def view_users():

# @app.route("/ratings_user")
# def view_ratings_user():

# @add.route("/modify_rating")
# def modify_rating():



if __name__=="__main__":
    app.run(debug=True)
