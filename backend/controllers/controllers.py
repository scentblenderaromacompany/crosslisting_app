from backend.models.models import db, Listing
from integrations.offerup.offerup_automation import create_offerup_listing
import os
import logging
from flask import request

def create_listing(data):
    try:
        # Save the listing in the database
        new_listing = Listing(
            title=data['title'],
            description=data['description'],
            price=data['price'],
            marketplace=', '.join(data['marketplace']),
            category=data['category'],
            condition=data['condition']
        )
        db.session.add(new_listing)
        db.session.commit()

        logging.info(f"Listing created: {new_listing}")

        # Get the list of image paths from the uploaded files
        image_paths = []
        for file in request.files.getlist('images'):
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            image_paths.append(file_path)

        # Check if OfferUp is one of the selected marketplaces
        if 'offerup' in data['marketplace']:
            # Send listing details to OfferUp automation, including images
            listing_data = {
                'title': data['title'],
                'description': data['description'],
                'price': data['price'],
                'image_paths': image_paths  # Pass the list of image paths
            }
            create_offerup_listing(listing_data)

    except Exception as e:
        logging.error(f"Error creating listing: {e}")
        raise
