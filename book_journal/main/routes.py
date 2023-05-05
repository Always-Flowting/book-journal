from flask import Blueprint, render_template
from sqlalchemy import select
from book_journal import db
from book_journal.models import Journal

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    posts = Journal.query.filter_by(public=True).order_by(Journal.date_posted.desc()).paginate(per_page=5)
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html')