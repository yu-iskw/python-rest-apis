import argparse
import requests
from time import time


def main(host, port):
    url = 'http://{host}:{port}/v1/predict'.format(host=host, port=port)
    data = {
        'sepal_length': 5.1,
        'sepal_width': 3.3,
        'petal_length': 1.7,
        'petal_width': 0.5,
    }
    n = 2000
    sum_time = 0.0
    for i in range(0, n):
        start_time = time()
        response = requests.post(url=url, data=data)
        sum_time += time() - start_time

    print(sum_time / n)
    # Check the status code.
    # print(response.status_code)
    # content = json.loads(response.content)
    # print(content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--host', type=str, help='host name', required=True)
    parser.add_argument('--port', type=int, help='port number', required=True)
    args = parser.parse_args()

    main(host=args.host, port=args.port)
