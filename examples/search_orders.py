# -*- coding: utf-8 -*-
import os
from flipkart import FlipkartAPI, Authentication

# Set authentication credentials
app_id = os.environ['FLIPKART_APP_ID']
app_secret = os.environ['FLIPKART_APP_SECRET']
auth = Authentication(app_id, app_secret, sandbox=True)

# Get an access token
token = auth.get_token_from_client_credentials()

# Get a flipkart client
flipkart = FlipkartAPI(token['access_token'], sandbox=True, debug=True)
response = list(flipkart.search_orders())

print "Number of orders: %d" % len(response)
