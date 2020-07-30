from flask import flash, redirect, render_template, url_for, session, request, Blueprint
from functools import wraps
from project.users.forms import LoginForm


users_blueprint = Blueprint('users', __name__, template_folder='templates')


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


# route for handling the login page logic
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    error = None
    if request.method == 'POST':
        if form.validate_on_submit():
            if (request.form['username'] != 'admin') \
                    or request.form['password'] != 'admin':
                error = 'Invalid Credentials. Please try again.'
            else:
                session['logged_in'] = True
                flash('You are logged in.')
                return redirect(url_for('home.home'))
        else:
            return render_template('login.html', form=form, error=error)
    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You are logged out.')
    return redirect(url_for('home.welcome'))
