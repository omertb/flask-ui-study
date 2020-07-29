from project import db
from project.models import User
from flask import flash, session, render_template, redirect, url_for, Blueprint
from functools import wraps

# home blueprint definition
home_blueprint = Blueprint('home', __name__, template_folder='templates')


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
@home_blueprint.route('/')
@login_required
def home():
    # return "Hello, World!"  # return a string
    posts = db.session.query(User).all()
    return render_template('home.html', posts=posts)  # render a template


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

