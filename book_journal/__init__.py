from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from book_journal.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login' # type: ignore
login_manager.login_message = 'info'
mail = Mail()

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    from book_journal.main.routes import main
    from book_journal.users.routes import users
    from book_journal.journals.routes import journals
    from book_journal.books.routes import books
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(journals)
    app.register_blueprint(books)

    from book_journal.tests.routes import tests
    app.register_blueprint(tests)

    return app