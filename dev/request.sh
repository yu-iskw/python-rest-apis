#!/bin/bash
set -e

HOST=$(docker-machine ip default)
HOST=0.0.0.0
PORT=8080
(echo -n '{"base64_image": "'; base64 ./tests/resources/test.jpg; echo '"}') |
  curl -H "Content-Type: application/json" -d @-  http://${HOST}:${PORT}/v1/predict
