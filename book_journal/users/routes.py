from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user
from book_journal import db, bcrypt
from book_journal.users.forms import RegistrationForm, LoginForm
from book_journal.models import User

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.password.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been succesfully created', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next', url_for('main.home'))
            return redirect(next_page)
        else:
            flash('Login Unsuccessful. Check email and password', 'danger')
    return render_template('login.html', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/account', methods=['GET', 'POST'])
def account():
    form = None
    return render_template('account.html', form=form)


@users.route('/user/<string:username>')
def user_journals(username):
    return render_template('user_journals.html')