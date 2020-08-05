from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user


def check_verified(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.verified is False:
            flash('Please verify your account!', 'warning')
            return redirect(url_for('users.unverified'))
        return func(*args, **kwargs)

    return decorated_function
