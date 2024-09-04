from backend.models.models import db
from app import create_app

app = create_app()

with app.app_context():
    db.create_all()
    print("Database initialized!")
