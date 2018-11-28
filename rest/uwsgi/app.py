import os

import numpy as np

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

# Create the flask application.
from rest.model.iris import IrisModel
from rest.utils import get_project_dir

app = Flask(__name__)
app.config.from_pyfile('./config.py')
api = Api(app)

# Load keras application
app.logger.info("start loading model")
model_path = os.path.join(get_project_dir(), 'model', 'iris.joblib')
model = IrisModel(model_path=model_path)
app.logger.info("end loading model")


class HealthCheckApi(Resource):
    """
    This class is used for health check.
    """
    def get(self):
        return {"status": "alive"}, 200


class MobileNetApi(Resource):

    # Define the inputs.
    parser = reqparse.RequestParser()
    parser.add_argument('sepal_length', type=float, help='sepal length', required=True)
    parser.add_argument('sepal_width', type=float, help='sepal width', required=True)
    parser.add_argument('petal_length', type=float, help='petal length', required=True)
    parser.add_argument('petal_width', type=float, help='petal width', required=True)
    parser.add_argument('threshold', type=float, help='threshold', required=False, default=0.5)

    def post(self):
        """Handle POST request."""
        args = self.__class__.parser.parse_args()
        sepal_length = args['sepal_length']
        sepal_width = args['sepal_width']
        petal_length = args['petal_length']
        petal_width = args['petal_width']

        try:
            X = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            result = model.predict(X)
            return jsonify(result)
        except Exception as e:
            return {"status": 404, "Error": "{}".format(e.message)}, 404


# Map paths
api.add_resource(MobileNetApi, '/v1/predict')
api.add_resource(HealthCheckApi, '/healthcheck')

if __name__ == '__main__':
    # Run App
    app.run(host='0.0.0.0', port='8080')
