from ebaysdk.trading import Connection as Trading
from ebaysdk.exception import ConnectionError
import logging

logging.basicConfig(level=logging.INFO)

def create_ebay_listing(listing):
    try:
        api = Trading(
            config_file=None,
            appid='YOUR_APP_ID',
            certid='YOUR_CERT_ID',
            devid='YOUR_DEV_ID',
            token='YOUR_OAUTH_TOKEN',
            siteid='0',
            warnings=True
        )
        response = api.execute('AddItem', {
            'Item': {
                'Title': listing.title,
                'Description': listing.description,
                'StartPrice': listing.price,
                'Currency': 'USD',
                'Country': 'US',
                'ConditionID': 1000,
                'ListingType': 'FixedPriceItem',
                'CategoryID': '11116',
                'PictureDetails': {
                    'PictureURL': listing.image_url
                },
                'Quantity': 1,
                'ReturnPolicy': {
                    'ReturnsAcceptedOption': 'ReturnsAccepted',
                    'RefundOption': 'MoneyBack',
                    'ReturnsWithinOption': 'Days_30',
                    'Description': 'If you are not satisfied, return the item for refund.',
                    'ShippingCostPaidByOption': 'Buyer'
                },
                'ShippingDetails': {
                    'ShippingServiceOptions': {
                        'ShippingServicePriority': 1,
                        'ShippingService': 'USPSMedia',
                        'ShippingServiceCost': 2.50
                    }
                },
                'Site': 'US'
            }
        })
        logging.info(f"eBay listing created: {response.dict()}")
        return response.dict()
    except ConnectionError as e:
        logging.error(f"Error creating eBay listing: {e}")
        raise
