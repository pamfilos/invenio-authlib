# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# Invenio-Authlib is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Minimal Flask application example.

SPHINX-START

First install Invenio-Authlib, setup the application and load
fixture data by running:

.. code-block:: console

   $ pip install -e .[all]
   $ cd examples
   $ ./app-setup.sh
   $ ./app-fixtures.sh

Next, start the development server:

.. code-block:: console

   $ export FLASK_APP=app.py FLASK_DEBUG=1
   $ flask run

and open the example application in your browser:

.. code-block:: console

    $ open http://127.0.0.1:5000/

To reset the example application run:

.. code-block:: console

    $ ./app-teardown.sh

SPHINX-END
"""

from __future__ import absolute_import, print_function

import os

from flask import Flask
from flask_babelex import Babel

from invenio_accounts import InvenioAccounts
from invenio_db import InvenioDB
from invenio_authlib import InvenioAuthlib
from invenio_authlib.views import blueprint

# Create Flask application
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'SQLALCHEMY_DATABASE_URI', 'sqlite:///app.db'
)

app.config.update(
    ACCOUNTS_USE_CELERY=False,
    # CELERY_ALWAYS_EAGER=True,
    # CELERY_CACHE_BACKEND='memory',
    # CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
    # CELERY_RESULT_BACKEND='cache',
    # MAIL_SUPPRESS_SEND=True,
    SECRET_KEY='CHANGE_ME',
    SECURITY_PASSWORD_SALT='CHANGE_ME_ALSO',
    # SQLALCHEMY_TRACK_MODIFICATIONS=False
)

Babel(app)
InvenioDB(app)
InvenioAccounts(app)
InvenioAuthlib(app)
app.register_blueprint(blueprint)
