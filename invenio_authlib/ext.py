# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# Invenio-Authlib is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module that adds more fun to the platform."""

from __future__ import absolute_import, print_function

from authlib.flask.client import OAuth

from . import config
from .utils import _fetch_token, _update_token


class InvenioAuthlib(object):
    """Invenio-Authlib extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        self.auth = OAuth(app,
                          fetch_token=_fetch_token,
                          update_token=_update_token)
        self.register_oauth_services()
        app.extensions['cap-auth'] = self

    def init_config(self, app):
        """Initialize configuration."""
        # Use theme's base template if theme is installed
        if 'BASE_TEMPLATE' in app.config:
            app.config.setdefault(
                'AUTHLIB_BASE_TEMPLATE',
                app.config['BASE_TEMPLATE'],
            )
        for k in dir(config):
            if k.startswith('AUTHLIB_'):
                app.config.setdefault(k, getattr(config, k))

    def register_oauth_services(self):
        for service in config.AUTHLIB_SERVICES:
            self.auth.register(**config.AUTHLIB_SERVICES[service])
