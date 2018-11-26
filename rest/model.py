#!/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import io
import base64

import numpy as np
from PIL import Image
import tensorflow as tf


class MobileNetModel(object):

    model = None

    def __init__(self):
        self.__class__.model = tf.keras.applications.mobilenet.MobileNet()

    @staticmethod
    def verify_image(image):
        image.verify()

    @staticmethod
    def preprocess(image, size=(224, 224)):
        # Resize image.
        image = image.resize(size, resample=Image.BICUBIC)
        # Convert to numpy.
        numpy_image = np.array(image)
        return numpy_image

    @staticmethod
    def base64_to_image(base64_image):
        return Image.open(io.BytesIO(base64.b64decode(base64_image)))

    @staticmethod
    def image_to_base64(image, format='JPEG'):
        in_mem_file = io.BytesIO()
        image.save(in_mem_file, format=format)
        # reset file pointer to start
        in_mem_file.seek(0)
        img_bytes = in_mem_file.read()
        base64_bstr = base64.b64encode(img_bytes)
        return base64_bstr.decode('ascii')

    def predict(self, base64_image):
        image = MobileNetModel.base64_to_image(base64_image)
        #MobileNetModel.verify_image(image)
        image = MobileNetModel.preprocess(image)
        image = image.reshape((1, 224, 224, 3))
        result = self.__class__.model.predict(image)
        return result[0]
