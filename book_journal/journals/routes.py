from flask import Blueprint, render_template
from book_journal.journals.forms import JournalForm

journals = Blueprint('journals', __name__)

@journals.route('/journal/new')
def new_journal():
    form = JournalForm()
    return render_template('journal.html', form=form)