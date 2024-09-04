import logging
from flask import Flask
from backend.models.models import db
from backend.config.config import Config

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database
    db.init_app(app)

    # Set up logging
    if not app.debug:
        logging.basicConfig(level=logging.INFO, filename='app.log', 
                            format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    else:
        logging.basicConfig(level=logging.DEBUG)

    with app.app_context():
        db.create_all()  # Create database tables if they don't exist

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'], host='0.0.0.0')
