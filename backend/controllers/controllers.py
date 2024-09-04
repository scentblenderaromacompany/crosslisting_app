import logging
from backend.models.models import db, Listing
from integrations.ebay.ebay_api import create_ebay_listing
from integrations.etsy.etsy_api import create_etsy_listing
from integrations.facebook.facebook_api import create_facebook_listing
from integrations.offerup.offerup_api import create_offerup_listing

logging.basicConfig(level=logging.INFO)

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

        for marketplace in data['marketplace']:
            try:
                if marketplace == 'ebay':
                    create_ebay_listing(new_listing)
                elif marketplace == 'etsy':
                    create_etsy_listing(new_listing)
                elif marketplace == 'facebook':
                    create_facebook_listing(new_listing)
                elif marketplace == 'offerup':
                    create_offerup_listing(new_listing)
                logging.info(f"Successfully listed on {marketplace}")
            except Exception as e:
                logging.error(f"Error listing on {marketplace}: {e}")

        return new_listing
    except Exception as e:
        logging.error(f"Error creating listing: {e}")
        raise

def get_all_listings():
    return Listing.query.all()
