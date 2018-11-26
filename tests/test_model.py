import os

import numpy as np
from PIL import Image

from rest.model import MobileNetModel

class TestMobileNetModel(object):

    test_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'resources', 'test.jpg'))

    def test_preprocessing(self):
        image = Image.open(self.__class__.test_image_path, 'r')
        result = MobileNetModel.preprocess(image)
        assert type(result) == np.ndarray
        assert result.shape == (224, 224, 3)

    def test_predict(self):
        model = MobileNetModel()
        image = Image.open(self.__class__.test_image_path, 'r')
        base64_image = MobileNetModel.image_to_base64(image)
        result = model.predict(base64_image)
        assert result.shape == (1000,)
