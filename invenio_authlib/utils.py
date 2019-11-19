# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# Invenio-Authlib is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module that adds more fun to the platform."""

from __future__ import absolute_import, print_function

from flask_login import current_user

from .models import OAuth2Token
from invenio_db import db


def _create_or_update_token(name, token):
    _token = OAuth2Token.get(name=name, user_id=current_user.id)
    if not _token:
        _token = OAuth2Token(name=name, user_id=current_user.id)
    _token.token_type = token.get('token_type', 'bearer')
    _token.access_token = token.get('access_token')
    _token.refresh_token = token.get('refresh_token')
    _token.expires_at = token.get('expires_at')

    return _token


def _fetch_token(name, user_id=None):
    if not user_id:
        user_id = current_user.id
    token = OAuth2Token.get(name=name, user_id=user_id)
    return token.to_token() if token else None


def _update_token(name, token):
    _token = _create_or_update_token(name, token)

    db.session.add(_token)
    db.session.commit()
    return _token
