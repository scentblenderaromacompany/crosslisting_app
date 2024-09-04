import unittest
from flask import Flask
from backend.models.models import db, Listing
from backend.controllers.controllers import create_listing

class TestCrossListingApp(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_listing(self):
        with self.app.app_context():
            data = {
                'title': 'Test Product',
                'description': 'This is a test product.',
                'price': 19.99,
                'image_url': 'http://example.com/test.jpg',
                'marketplace': ['ebay', 'etsy', 'facebook', 'offerup'],
                'category': 'Electronics',
                'condition': 'New'
            }
            listing = create_listing(data)
            self.assertIsNotNone(listing)
            self.assertEqual(listing.title, 'Test Product')
            self.assertEqual(listing.price, 19.99)
            self.assertIn('ebay', listing.marketplace)

if __name__ == '__main__':
    unittest.main()
