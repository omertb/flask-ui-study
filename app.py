from flask import Flask, flash, session, render_template, redirect, url_for
from functools import wraps
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# config
app.config.from_object('config.DevelopmentConfig')

# create the sqlalchemy object
db = SQLAlchemy(app)

# import db schema
from models import *
from project.users.views import users_blueprint

app.register_blueprint(users_blueprint)


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap


# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    # return "Hello, World!"  # return a string
    posts = db.session.query(User).all()
    return render_template('home.html', posts=posts)  # render a template


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run()