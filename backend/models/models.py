import logging
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    condition = db.Column(db.String(20), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"Listing('{self.title}', '{self.price}')"

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            logging.info(f"Listing saved: {self.title} at {self.price}")
        except Exception as e:
            logging.error(f"Failed to save listing: {e}")
