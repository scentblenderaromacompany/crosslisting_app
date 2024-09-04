from flask import Blueprint, render_template, request, redirect, url_for, flash
from backend.controllers.controllers import create_listing, get_all_listings

main = Blueprint('main', __name__)

@main.route('/')
def index():
    listings = get_all_listings()
    return render_template('index.html', listings=listings)

@main.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            data = {
                'title': request.form['title'],
                'description': request.form['description'],
                'price': request.form['price'],
                'image_url': request.form['image_url'],
                'marketplace': request.form.getlist('marketplace'),
                'category': request.form['category'],
                'condition': request.form['condition']
            }
            create_listing(data)
            flash('Listing created successfully!', 'success')
            return redirect(url_for('main.index'))
        except Exception as e:
            flash(f'Error creating listing: {e}', 'danger')
    return render_template('create.html')
