import os

import numpy as np
from PIL import Image

from rest.model.mobilenet import MobileNetModel


class TestMobileNetModel(object):

    test_image_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'resources', 'test.jpg'))

    def test_preprocessing(self):
        image = Image.open(self.__class__.test_image_path, 'r')
        result = MobileNetModel.preprocess(image)
        assert type(result) == np.ndarray
        assert result.shape == (1, 224, 224, 3)

    def test_predict(self):
        model = MobileNetModel()
        image = Image.open(self.__class__.test_image_path, 'r')
        # image = MobileNetModel.preprocess(image)
        result = model.predict(image, top=9)
        assert type(result) == dict
        assert 'labels' in result.keys()
        assert 'scores' in result.keys()
        assert 'inference_time' in result.keys()
        assert len(result['labels']) == 9
        assert len(result['scores']) == 9
