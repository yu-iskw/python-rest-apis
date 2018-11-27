import json
import os

from PIL import Image

from rest.model.mobilenet import MobileNetModel
from rest.uwsgi.app import app


class TestMobileNetApi(object):

    test_image_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'resources', 'test.jpg')
    )

    def test_healthcheck(self):
        client = app.test_client()
        response = client.get('/healthcheck')
        assert response.status_code == 200

    def test_post(self):
        # Read and convert image.
        image = Image.open(self.__class__.test_image_path, 'r')
        base64_image = MobileNetModel.image_to_base64(image)

        # Request POST method.
        client = app.test_client()
        url = "/v1/predict"
        data = {
            'sepal_length': 5.1,
            'sepal_width': 3.3,
            'petal_length': 1.7,
            'petal_width': 0.5,
        }
        response = client.post(url, data=data)
        response_json = json.loads(response.data.decode('utf8'))
        assert 'prediction' in response_json.keys()
        assert 'inference_time' in response_json.keys()
