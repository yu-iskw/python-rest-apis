#!/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import io
import base64

import numpy as np
from PIL import Image
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import tensorflow as tf

import traceback

# Create the flask application.

app = Flask(__name__)
app.config.from_pyfile('./config.py')
api = Api(app)

# Load keras application
model = tf.keras.applications.mobilenet.MobileNet()


class HealthCheckApi(Resource):
    """
    This class is used for health check.
    """
    def get(self):
        return {"status": "alive"}, 200


class MobileNetApi(Resource):

    # Init variables
    def __init__(self):
        # Request parser
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('base64_image', type=str, required=True, help='BASE64 image')
        self.parser = parser

    def post(self):
        """Handle POST request."""
        args = self.parser.parse_args()

        base64_image = args['base64_image']
        try:
            image = self._preprocess(base64_image)
            return {"status": "alive"}, 200
        except Exception as e:
            return {"status": 404, "Error": "{}".format(e.message)}, 404

    def _preprocess(self, base64_image, size=(224, 224, 3)):
        image = Image.open(io.BytesIO(base64.b64decode(base64_image)))
        # Verify image.
        image.verify()
        # Resize image.
        image.resize(size, resample=Image.BICUBIC)
        # Convert to numpy.
        numpy_image = np.array(image)
        return numpy_image


# Map paths
api.add_resource(MobileNetApi, '/v1.0/predict')
api.add_resource(HealthCheckApi, '/healthcheck')

if __name__ == '__main__':
    # Run App
    app.run(host='0.0.0.0', port='8080')
