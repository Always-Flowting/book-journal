from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import current_user, login_required, login_user, logout_user
from book_journal import db, bcrypt
from book_journal.users.forms import AccountForm, RegistrationForm, LoginForm
from book_journal.models import User

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
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
@login_required
def account():
    form = AccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.password.data and form.new_password.data:
            current_user.password = bcrypt.generate_password_hash(form.new_password.data)
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    form.username.data = current_user.username # type: ignore
    form.email.data = current_user.email # type: ignore
    return render_template('account.html', form=form)


@users.route('/user/<string:username>')
def user_journals(username):
    return render_template('user_journals.html')