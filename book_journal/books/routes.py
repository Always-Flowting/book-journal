from flask import Blueprint, jsonify, request, render_template
from book_journal.books.forms import BookForm

books = Blueprint('books', __name__)


@books.route('/book/search', methods=['POST'])
def search_books():
    books = ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'The Catcher in the Rye']
    data = request.get_json()
    return jsonify({'books': [data.get('search_term')]})


@books.route('/book/new', methods=['POST', 'GET'])
def new_book():
    form = BookForm()

    is_modal_raw = request.args.get('modal')
    is_modal = False
    if is_modal_raw:
        is_modal = is_modal_raw.lower() == 'true'
    if is_modal:
        return render_template('book_form.html', form=form, is_modal=is_modal)
    else:
        return render_template('book.html', form=form)