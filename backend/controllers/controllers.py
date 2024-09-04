from backend.models.models import db, Listing
import logging

def create_listing(data):
    try:
        new_listing = Listing(
            title=data['title'],
            description=data['description'],
            price=data['price'],
            image_url=data['image_url'],
            marketplace=', '.join(data['marketplace']),
            category=data['category'],
            condition=data['condition']
        )
        db.session.add(new_listing)
        db.session.commit()
        logging.info(f"Listing created: {new_listing}")
    except Exception as e:
        logging.error(f"Error creating listing: {e}")
        raise

def get_all_listings():
    return Listing.query.all()
