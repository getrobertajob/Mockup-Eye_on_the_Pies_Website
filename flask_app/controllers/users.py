# Imports needed resources
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

# setup for Bcrypt
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


# Initial route, first page that loads
# renders user registration and log in
@app.route("/")
def index():




    test_user=1
    print("------------------")
    print("------------------")
    print(type(test_user))
    print("------------------")
    print("------------------")











    return render_template("index.html")


# route to register a new user
# triggered by clicking on submit button
@app.route("/register", methods=["POST"])
def register():
    # sends form data to validate user registration
    if not User.validate_register(request.form):
        # redirect to same page if vaidation fails
        return redirect("/")
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    # sends form data to save if validation check passed
    id = User.save(data)
    session["user_id"] = id
    return redirect("/dashboard")


# route to log in user
# triggered by clicking on log in button
@app.route("/login", methods=["POST"])
def login():
    # sends form data to get by email
    # gets user data based on provided email
    user = User.get_by_email(request.form)
    # checks if email matches an account
    if not user:
        flash("User account not found", "login")
        return redirect("/")
    # checks if password matches that account
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Invalid Password", "login")
        return redirect("/")
    session["user_id"] = user.id
    return redirect("/dashboard")


# route to clear session and log out user
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
