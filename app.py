################################################################
#
#   Main Street
#   CS146 19F Final Project
#   Kyla Barry, Julie (Min Jee) Cheon, Daniel Claro, Johnny Wong
#
################################################################
import os

from flask import Flask, render_template, redirect, url_for, session, request, flash, get_flashed_messages

from utils import db

#-----------instantiate Flask Object-----------
app = Flask(__name__)
app.secret_key = os.urandom(32)

DB_FILE = "data/street.db"
db.create_db()

@app.route("/")
def login():
    '''Index is login page'''
    if "username" in session:
        return redirect(url_for("home"))
    return render_template('index.html')

@app.route("/register")
def register():
    '''Register Page'''
    return render_template('register.html')

@app.route("/auth", methods=["POST"])
def auth():
    '''Authentication for login/register'''
    formType = request.form["submit"]
    username, password = request.form["username"], request.form["password"]
    print("Username: ", username)
    print("Password: ", password)
    # Handle Login request
    if formType == "Login":
        # verify user
        if len(username.strip()) != 0 and len(password.strip()) != 0 and db.verify_user(username, password):
            session["username"] = username
            return redirect(url_for("home"))
        # user found but password incorrect
        elif db.find_user(username):
            flash("Incorrect password!")
        # user not found at all
        else:
            flash("Incorrect credentials!")
            print('owo')
    # Handle Register request
    else:
        if db.find_user(username):
            flash("Username taken!")
            return redirect(url_for("register"))
        elif len(username.strip()) == 0 or ' ' in username:
            flash("Invalid username!")
            return redirect(url_for("register"))
        elif len(password.strip()) == 0 or ' ' in password:
            flash("Invalid password!")
            return redirect(url_for("register"))
        hobbies = request.form["hobbies"]
        email, socials, phone = request.form["email"].strip(), request.form.getlist("socials"), request.form["phone"].strip()
        socials = list(map(lambda str: str.strip(), socials))
        strOfSocials = ""
        for handle in socials:
            strOfSocials += handle
        print("Email:", email)
        print("Socials:", strOfSocials)
        print("Phone:", phone)
        db.add_profile(username, hobbies, email, strOfSocials, phone)
        db.register_user(username, password)
        flash("{} has been registered".format(username))
    return redirect(url_for("login"))


@app.route("/profile")
def profile():
    '''Get profile page for username'''
    if "username" not in session:
        return redirect(url_for("login"))
    profileInfo = db.get_profile(session["username"])
    print(profileInfo)
    username = session["username"]
    hobbies = [profileInfo["hobbies"]]
    email = profileInfo["email"]
    socials = profileInfo["socials"]
    phone = profileInfo["phone"]

    return render_template("profile.html", username=username, hobbyList=hobbies, email=email, socials=socials, phone=phone)

@app.route("/home")
def home():
    '''Get home page'''
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("home.html")


@app.route("/logout")
def logout():
    '''Logs user out'''
    if "username" not in session:
        return redirect(url_for("login"))
    session.pop("username", None)
    flash("Successfully logged out!")
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.debug = True
    app.run()
