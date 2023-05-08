from flask import Blueprint, jsonify

books = Blueprint('books', __name__)


@books.route('/book/search', methods=['POST'])
def search_books():
    books = [{'title': 'The Great Gatsby'},
             {'title': 'To Kill a Mockingbird'},
             {'title': '1984'},
             {'title': 'The Catcher in the Rye'}]
    return jsonify({'books': books})