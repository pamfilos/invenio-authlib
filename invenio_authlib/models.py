# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# Invenio-Authlib is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module that adds more fun to the platform."""

from invenio_db import db
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from sqlalchemy.dialects import postgresql
from sqlalchemy_utils.types import JSONType

json_type = JSONType().with_variant(
    postgresql.JSONB(none_as_null=True),
    'postgresql',
).with_variant(
    JSONType(),
    'sqlite',
)

# class OAuth1Token(db.Model):
#     id = db.Column(db.Integer, primary_key=True)

#     user_id = db.Column(db.Integer, nullable=False)
#     name = db.Column(db.String(20), nullable=False)

#     oauth_token = db.Column(db.String(48), nullable=False)
#     oauth_token_secret = db.Column(db.String(48))

#     def to_token(self):
#         return dict(
#             oauth_token=self.access_token,
#             oauth_token_secret=self.alt_token,
#         )

#     @classmethod
#     def get(cls, name, user_id):
#         """Get schema by name and version."""

#         try:
#             token = cls.query \
#                 .filter_by(name=name, user_id=user_id) \
#                 .one()

#         except (NoResultFound, MultipleResultsFound):
#             return None

#         return token


class OAuth2Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), nullable=False)

    token_type = db.Column(db.String(20))
    access_token = db.Column(db.String(), nullable=False)
    refresh_token = db.Column(db.String())
    expires_at = db.Column(db.BigInteger, default=0)
    expires_in = db.Column(db.BigInteger, default=0)

    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, server_default=db.func.now(),
                        server_onupdate=db.func.now())

    extra_data = db.Column(json_type,
                           default=lambda: {},
                           nullable=True)

    def to_token(self):
        return dict(
            access_token=self.access_token,
            token_type=self.token_type,
            refresh_token=self.refresh_token,
            expires_at=self.expires_at,
            expires_in=self.expires_in,
        )

    @classmethod
    def get(cls, name, user_id):
        """Get schema by name and version."""

        try:
            token = cls.query \
                .filter_by(name=name, user_id=user_id) \
                .one()

        except (NoResultFound, MultipleResultsFound):
            return None

        return token
