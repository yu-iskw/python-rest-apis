import os

from time import time
import status
import numpy as np

from tornado import web
from tornado.escape import json_decode

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

    # def prepare(self):
    #     if self.request.headers.get('Content-Type') != 'application/json':
    #         raise HTTPError(status.HTTP_406_NOT_ACCEPTABLE)

    def post(self):
        response = {}
        try:
            # Get request body.
            request_json = json_decode(self.request.body)
            sepal_length = request_json['sepal_length']
            sepal_width = request_json['sepal_width']
            petal_length = request_json['petal_length']
            petal_width = request_json['petal_width']

            # Predict.
            X = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            response = model.predict(X)

            # Make the response.
            self.set_status(status.HTTP_200_OK)
            self.write(response)
        except Exception as e:
            response = {"message": e}
            self.set_status(status.HTTP_400_BAD_REQUEST)
            self.write(response)


def make_app(host='localhost'):
    return web.Application([
        (r"/v1/predict", IrisPredictHandler),
        (r"/healthcheck", HealthCheckHandler),
    ], default_host=host)


# if __name__ == "__main__":
#     define('host', default='localhost', help='host')
#     define('port', default=8080, help='port to listen on')
#
#     application = make_app(host=options.host)
#     application.listen(options.port)
#     ioloop.IOLoop.current().start()
