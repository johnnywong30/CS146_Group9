################################################################
#
#   Main Street
#   CS146 19F Final ProjectProject
#   Kyla Barry, Julie (Min Jee) Cheon, Daniel Claro, Johnny Wong
#
################################################################
import os

from flask import Flask, render_template, redirect, url_for, session, request, flash, get_flashed_messages

# from util import db

#-----------instantiate Flask Object-----------
app = Flask(__name__)
app.secret_key = os.urandom(32)

# DB_FILE = "data/street.db"
# db.create_db()

@app.route("/")
def login():
    '''Index is login page'''
    return render_template('index.html')

@app.route("/register")
def register():
    '''Register Page'''
    return render_template('register.html')

@app.route("/auth")
def auth():
    '''Authentication for login/register'''
    pass

@app.route("/user/<username>")
def profile():
    '''Get profile page for username'''
    pass

@app.route("/home")
def home():
    '''Get home page'''
    pass



@app.route("/")


if __name__ == "__main__":
    app.debug = True
    app.run()
