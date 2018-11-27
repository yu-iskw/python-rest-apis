#!/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import os

import numpy as np

from rest.model.iris import IrisModel


class TestIrisModel(object):

    def test_predict(self):
        model_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "model", "iris.joblib"))
        model = IrisModel(model_path=model_path)
        X = np.expand_dims([5.1, 3.3, 1.7, 0.5], axis=0)
        result = model.predict(X)
        assert result['prediction'] == 0
        assert 'inference_time' in result.keys()
