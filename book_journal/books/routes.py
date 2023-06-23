from flask import Blueprint, jsonify, request

books = Blueprint('books', __name__)


@books.route('/book/search', methods=['POST'])
def search_books():
    books = ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'The Catcher in the Rye']
    data = request.get_json()
    return jsonify({'books': [data.get('search_term')]})