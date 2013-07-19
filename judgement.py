from flask import Flask, render_template, redirect, request
import model 

app = Flask(__name__)

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)


@app.route("/new_user")
def get_user():
    #print "wtf people"
    return render_template("new_user.html")


@app.route("/create_user", methods = ["POST", "GET"])
def create_user():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        age = request.form.get("age")
        zipcode = request.form.get("zipcode")
        new_user = model.User(email=email, password=password, age=age, zipcode=zipcode)
        model.session.add(new_user)
        model.session.commit()
        return redirect("/display_user") 
    else:
        return redirect("/punch_user")


@app.route("/display_user")
def display_user():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)


@app.route("/get_user_email")
def get_user_email():
    return render_template("get_user_email.html")

@app.route("/view_user", methods = ["POST", "GET"])
def view_user():

    user= model.session.query(model.User).filter_by(email = request.form["email"]).one()
    # return user
    print user, "THIS THIS HTIS #####################FUCK#############################"
    # return "I AM RETURNING HERE A USER"
    return render_template("display_user_by_email.html", user=user)


# make page that displays ratings by email
@app.route("/display_user_by_email", methods = ["POST", "GET"])
def display_user():
    user_list = model.session.query(model.User).limit(5).all()


@app.route("/punch_user")
def punch_face():

    return "you failed and should try again."


@app.route("/login_page")
def user_login():
    return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        print "LOGIN EMAIL IS: ", request.form["email"]
        print "LOGIN PASSWORD IS: ", request.form["password"]
            
        user =  session.query(model.User).filter_by(email = request.form["email"], password=request.form["password"]).one()
        session["user_id"] = user.id 
    return redirect("/punch_user")


# @app.route("/ratings_user")
# def view_ratings_user():

# @add.route("/modify_rating")
# def modify_rating():



if __name__=="__main__":
    app.run(debug=True)
