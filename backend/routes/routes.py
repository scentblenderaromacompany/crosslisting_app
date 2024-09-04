import logging
from flask import Blueprint, render_template, request, redirect, url_for, flash
from backend.models.models import db, Listing

main = Blueprint('main', __name__)

@main.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            # Get form data
            title = request.form['title']
            description = request.form['description']
            price = request.form['price']
            category = request.form['category']
            condition = request.form['condition']
            image_url = request.form['image_url']

            # Create a new listing
            new_listing = Listing(
                title=title,
                description=description,
                price=price,
                category=category,
                condition=condition,
                image_url=image_url
            )
            
            # Save the listing
            new_listing.save()

            # Log and redirect
            logging.info(f"New listing created: {title}")
            flash("Listing created successfully!", "success")
            return redirect(url_for('main.create'))
        except Exception as e:
            logging.error(f"Failed to create listing: {e}")
            flash("Failed to create listing.", "danger")

    return render_template('create.html')
