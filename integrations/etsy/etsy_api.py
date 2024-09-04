import requests
import logging
import time

logging.basicConfig(level=logging.INFO)

def create_etsy_listing(listing):
    url = 'https://openapi.etsy.com/v2/listings'
    headers = {
        'x-api-key': 'YOUR_ETSY_API_KEY',
        'Authorization': 'Bearer YOUR_OAUTH_TOKEN',
        'Content-Type': 'application/json'
    }
    data = {
        'title': listing.title,
        'description': listing.description,
        'price': listing.price,
        'quantity': 1,
        'who_made': 'i_did',
        'is_supply': 'false',
        'when_made': '2020_2024',
        'image_url': listing.image_url
    }

    for attempt in range(3):  # Retry up to 3 times
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            logging.info(f"Etsy listing created: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error creating Etsy listing: {e}")
            time.sleep(5)  # Wait before retrying
    raise Exception("Failed to create Etsy listing after multiple attempts.")
