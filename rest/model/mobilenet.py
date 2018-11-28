import io
import base64
from time import time

import numpy as np
from PIL import Image
import tensorflow as tf
from keras_applications.mobilenet import preprocess_input
from keras_preprocessing.image import img_to_array
from tensorflow.python.keras.applications.mobilenet import decode_predictions


class MobileNetModel(object):

    model = None

    def __init__(self):
        # Load MobileNet as a class variable.
        if self.__class__.model is None:
            self.__class__.model = tf.keras.applications.mobilenet.MobileNet()

    @staticmethod
    def verify_image(image):
        image.verify()

    @staticmethod
    def preprocess(image, size=(224, 224)):
        """Preprocess image.

        :param image: PIL image
        :param size: resize size
        :return: numpy.ndarray
        """
        # Resize image.
        # image = image.resize(size, resample=Image.BICUBIC)
        image = image.resize(size)
        # Convert to numpy.
        numpy_image = img_to_array(image)
        # Reshape for MobileNet
        numpy_image = np.expand_dims(numpy_image, axis=0)
        numpy_image = preprocess_input(numpy_image, backend=tf.keras.backend)
        return numpy_image

    @staticmethod
    def base64_to_image(base64_image):
        """Convert BASE64 string to pillow image."""
        return Image.open(io.BytesIO(base64.b64decode(base64_image)))

    @staticmethod
    def image_to_base64(image, format='JPEG'):
        """Convert pillow image to BASE64 string."""
        in_mem_file = io.BytesIO()
        image.save(in_mem_file, format=format)
        # reset file pointer to start
        in_mem_file.seek(0)
        img_bytes = in_mem_file.read()
        base64_bstr = base64.b64encode(img_bytes)
        return base64_bstr.decode('ascii')

    def predict(self, image, top=5):
        """Predict with MobileNet."""
        start_time = time()

        # Prepfocess
        image = MobileNetModel.preprocess(image)
        # Predict
        predictions = self.__class__.model.predict(image)
        # Decode predictions.
        decoded_predictions = decode_predictions(predictions, top=top)[0]
        results = {
            'labels': [],
            'scores': [],
            'inference_time': time() - start_time
        }
        for i in range(0, len(decoded_predictions)):
            results['labels'].append(decoded_predictions[i][1])
            results['scores'].append(float(decoded_predictions[i][2]))
        return results
