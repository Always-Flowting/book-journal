from flask import Flask
from book_journal.config import Config


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    from book_journal.main.routes import main
    app.register_blueprint(main)

    return app