======================================
Python Flipkart Marketplace API Client
======================================

.. image:: https://img.shields.io/travis/fulfilio/python-flipkart.svg
        :target: https://travis-ci.org/fulfilio/python-flipkart

.. image:: https://img.shields.io/pypi/v/python-flipkart.svg
        :target: https://pypi.python.org/pypi/python-flipkart


Python Flipkart Marketplace API Client

* Free software: BSD license
* Documentation: https://python-flipkart.readthedocs.org.

Installing
----------

From PYPI:

.. code-block:: shell

   $ pip install python-flipkart

From source code (advanced users and for development):

.. code-block:: shell

   $ git clone https://github.com/fulfilio/python-flipkart.git
   $ cd python-flipkart
   $ python setup.py install


Example Usage
-------------

.. code-block:: python

    from flipkart import FlipkartAPI, Authentication

    auth = Authentication('app id', 'app secret', sandbox=True)
    token = auth.get_token_from_client_credentials()

    flipkart = FlipkartAPI(token['access_token'], sandbox=True, debug=True)
    orders = flipkart.search_orders()


Get listings of a SKU
`````````````````````

.. code-block:: python

    sku = flipkart.sku('my-special-sku', fsn='TSHDBN3326TEZHQZ')
    for listing in sku.listings:
        print listing.attributes['mrp']


Create a listing
````````````````

.. code-block:: python

    sku = flipkart.sku('my-special-sku', fsn='TSHDBN3326TEZHQZ')
    listing = sku.create_listing(
        mrp=2400,
        selling_price=2300,
        listing_status="INACTIVE",
        fulfilled_by="seller",
        national_shipping_charge=20,
        zonal_shipping_charge=20,
        local_shipping_charge=20,
        procurement_sla=3,
        stock_count=23,
    )
    listing.save()
    print listing.mrp

Update a listing
````````````````

.. code-block:: python

    listing = flipkart.listing('LSTTSHDBN332XDYBZ5MHX30XI')
    listing.attributes['mrp'] = 2600
    listing.save()


Searching for orders
````````````````````

.. code-block:: python

    orders = flipkart.search_orders()

Find only orders of selected SKUs:

.. code-block:: python

    orders = flipkart.search_orders(
        filters={'sku': ['my-sku-1', 'my-sku-2']}
    )

Filter by state:

.. code-block:: python

    orders = flipkart.search_orders(
        filters={'states': ['Approved']}
    )

.. tip::

   For a list of valid state see `API documentation 
   <https://seller.flipkart.com/api-docs/order-api-docs/OMAPIOverview.html>`_

Fetching a specific order item
``````````````````````````````

.. code-block:: python

    order_item = flipkart.order_item('')



Getting Access Token
````````````````````

If you have registered an application with your seller credentials and
would like to access resources in your account, you could use the
application id and secret alone to do so. The authentication helper in the
API gives you a convenient way to get tokens

.. code-block:: python

    from auth import Authentication

    auth = Authentication(
        '<application id>',
        '<application secret>',
        sandbox=True,           # If you are using sandbox
    )
    auth.get_token_from_client_credentials()

Features
--------

* TODO
