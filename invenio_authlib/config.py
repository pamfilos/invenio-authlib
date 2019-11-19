# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# Invenio-Authlib is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module that adds more fun to the platform."""

import os
# TODO: This is an example file. Remove it if your package does not use any
# extra configuration variables.

AUTHLIB_DEFAULT_VALUE = 'foobar'
"""Default value for the application."""

AUTHLIB_BASE_TEMPLATE = 'invenio_authlib/base.html'
"""Default base template for the demo page."""

# HOW TO USE
# ==========
#
# Authlib's Flask OAuth registry can load the configuration from
# Flask app.config automatically
# Check: https://docs.authlib.org/en/latest/client/flask.html#configuration
# They can be configured in your Flask App configuration
# Config key is formatted with {name}_{key} in uppercase, e.g.

# EXAMPLE_CLIENT_ID	OAuth Consumer Key
# EXAMPLE_CLIENT_SECRET	OAuth Consumer Secret
# or for Invenio purposes, like
# INVENIO_EXAMPLE_CLIENT_ID	OAuth Consumer Key
# INVENIO_EXAMPLE_CLIENT_SECRET	OAuth Consumer Secret


def orcid_extra_data(client, token):
    return {"orcid_name": token.get("name"), "orcid_id": token.get("orcid")}


AUTHLIB_SERVICES = {
    "GITHUB":
    dict(
        name='github',
        client_id=os.getenv('GITHUB_CLIENT_ID'),
        client_secret=os.getenv('GITHUB_CLIENT_SECRET'),
        access_token_url='https://github.com/login/oauth/access_token',
        authorize_url='https://github.com/login/oauth/authorize',
        api_base_url='https://api.github.com/',
        client_kwargs={'scope': 'repo,public_repo:'},
    ),
    "ZENODO":
    dict(
        name='zenodo',
        client_id=os.getenv('ZENODO_CLIENT_ID'),
        client_secret=os.getenv('ZENODO_CLIENT_SECRET'),
        access_token_url='https://zenodo.org/oauth/token',
        authorize_url='https://zenodo.org/oauth/authorize',
        api_base_url='https://zenodo.org/',
        client_kwargs={
            'scope': 'deposit:write deposit:actions',
            'token_endpoint_auth_method': 'client_secret_post',
            'token_placement': 'uri'
        },
    ),
    "GITLAB":
    dict(
        name='gitlab',
        client_id=os.getenv('GITLAB_CLIENT_ID'),
        client_secret=os.getenv('GITLAB_CLIENT_SECRET'),
        access_token_url='https://gitlab.cern.ch/oauth/token',
        authorize_url='https://gitlab.cern.ch/oauth/authorize',
        api_base_url='https://gitlab.cern.ch/api/v4/',
        client_kwargs={'scope': 'api'},
    ),
    "CERN": dict(
        name='cern',
        client_id=os.getenv('CERN_CLIENT_ID'),
        client_secret=os.getenv('CERN_CLIENT_SECRET'),
        access_token_url='https://oauth.web.cern.ch/OAuth/Token',
        authorize_url='https://oauth.web.cern.ch/OAuth/Authorize',
        api_base_url='https://oauthresource.web.cern.ch/api/',
        client_kwargs={
            'scope': 'read:user',
            'token_endpoint_auth_method': 'client_secret_post',
        }
    ),
    "ORCID":
    dict(name='orcid',
         client_id=os.getenv('ORCID_CLIENT_ID'),
         client_secret=os.getenv('ORCID_CLIENT_SECRET'),
         access_token_url='https://orcid.org/oauth/token',
         authorize_url='https://orcid.org/oauth/authorize',
         api_base_url='https://pub.orcid.org/v2.0',
         client_kwargs={
             'scope': '/authenticate',
             'token_endpoint_auth_method': 'client_secret_post'
         },
         extra_data_method=orcid_extra_data)
}
