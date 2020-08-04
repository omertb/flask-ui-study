from flask import flash, redirect, render_template, url_for, request, Blueprint
from project.users.forms import LoginForm, RegisterForm
from project.models import User, bcrypt
from project import db
from flask_login import login_user, login_required, logout_user
from project.token import generate_verification_token, verify_token
from project.email import send_email


users_blueprint = Blueprint('users', __name__, template_folder='templates')


# login page
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    error = None
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
                # session['logged_in'] = True
                login_user(user)  # (flask_login) session created
                flash('You are logged in.')
                return redirect(url_for('home.home'))
            else:
                error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/logout')
@login_required  # flask_login
def logout():
    logout_user()  # (flask_login) clear session
    flash('You are logged out.')
    return redirect(url_for('home.welcome'))


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            username=form.email.data.split("@")[0],
            password=form.password.data,
            verified=False
        )
        db.session.add(user)
        db.session.commit()

        token = generate_verification_token(user.email)

        verification_url = url_for('users.verify_email', token=token, _external=True)
        html = render_template('activate.html', verification_url=verification_url)
        subject = "Please verify your email"
        send_email(user.email, subject, html)

        login_user(user)
        flash("Verification email has been sent via email", "success")

        return redirect(url_for('home.home'))

    return render_template('register.html', form=form)


@users_blueprint.route('/verify/<token>')
@login_required
def verify_email(token):
    try:
        email = verify_token(token)
    except:
        flash('Verification link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.verified:
        flash('Account already verified. Please login.', 'success')
    else:
        user.verified = True
        db.session.add(user)
        db.session.commit()
        flash('You have verified your account. Thanks!', 'success')
    return redirect(url_for('home.home'))
