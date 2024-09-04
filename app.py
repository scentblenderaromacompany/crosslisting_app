from flask import Flask
from backend.routes.routes import main
from backend.models.models import db
from backend.config.config import Config
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    
    # Load configuration settings from config.py
    app.config.from_object(Config)

    # Initialize the database connection
    db.init_app(app)

    # Create all the database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Register the main blueprint for routing
    app.register_blueprint(main)

    return app

if __name__ == '__main__':
    # Create the app and run it
    app = create_app()

    # Run the app with the configuration set in the .env file
    app.run(debug=os.getenv('FLASK_DEBUG', 'false').lower() == 'true', host='0.0.0.0')
