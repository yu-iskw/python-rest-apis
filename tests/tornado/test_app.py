#!/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

# compatible importing urllib for python2 and 3.
from future.standard_library import install_aliases
install_aliases()
from urllib.parse import urlencode  # noqa: E402

from tornado.testing import AsyncHTTPTestCase  # noqa: E402
from rest.tornado import app  # noqa: E402


class TestMainHandler(AsyncHTTPTestCase):

    def get_app(self):
        return app.make_app()

    def test_homepage(self):
        data = {}
        data = urlencode(data)
        response = self.fetch('/', method='POST', body=data)
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'{"message": "hello"}')
