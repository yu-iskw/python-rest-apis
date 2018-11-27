#!/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import os

import status
import numpy as np

import tornado.ioloop
from tornado import web
from tornado.options import define, options

from rest.model.iris import IrisModel
from rest.utils import get_project_dir

# Load model
model_path = os.path.join(get_project_dir(), 'model', 'iris.joblib')
model = IrisModel(model_path=model_path)


class HealthCheckHandler(web.RequestHandler):

    def get(self):
        response = {"status": "alive"}
        self.set_status(status.HTTP_200_OK)
        self.write(response)


class IrisPredictHandler(web.RequestHandler):
    # SUPPORTED_METHODS = ("POST")

    def post(self):
        response = {}
        try:
            sepal_length = self.get_argument('sepal_length')
            sepal_width = self.get_argument('sepal_width')
            petal_length = self.get_argument('petal_length')
            petal_width = self.get_argument('petal_width')

            X = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            result = model.predict(X)
            response = result
            self.set_status(status.HTTP_200_OK)
            self.write(response)
        except Exception as e:
            response = {"message": e}
            self.set_status(status.HTTP_400_BAD_REQUEST)
            self.write(response)


def make_app(host='localhost'):
    return tornado.web.Application([
        (r"/v1/predict", IrisPredictHandler),
        (r"/healthcheck", HealthCheckHandler),
    ], default_host=host)


if __name__ == "__main__":
    define('host', default='localhost', help='host')
    define('port', default=8080, help='port to listen on')

    application = make_app(host=options.host)
    application.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
