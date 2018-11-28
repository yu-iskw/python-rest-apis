#!/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import json
import status

from tornado.testing import AsyncHTTPTestCase
from rest.tornado_app import app

# compatible importing urllib for python2 and 3.
from future.standard_library import install_aliases
install_aliases()
from urllib.parse import urlencode  # noqa: E402


class TestHealthCheckHandler(AsyncHTTPTestCase):
    def get_app(self):
        return app.make_app()

    def test_get(self):
        response = self.fetch('/healthcheck')
        assert response.code == status.HTTP_200_OK


class TestIrisPredictorHandler(AsyncHTTPTestCase):

    def get_app(self):
        return app.make_app()

    def test_post_with_valid_params(self):
        headers = {'Content-Type': 'application/json'}
        data = {
            'sepal_length': 5.1,
            'sepal_width': 3.3,
            'petal_length': 1.7,
            'petal_width': 0.5,
        }
        data = json.dumps(data).encode('utf-8')
        response = self.fetch('/v1/predict', method='POST', headers=headers, body=data)
        response_json = json.loads(response.body)
        assert response.code == status.HTTP_200_OK
        assert response_json['prediction'] == 0
        assert response_json['inference_time'] is not None

    def test_post_with_invalid_params(self):
        data = {}
        data = urlencode(data)
        response = self.fetch('/v1/predict', method='POST', body=data)
        assert response.code == status.HTTP_500_INTERNAL_SERVER_ERROR
