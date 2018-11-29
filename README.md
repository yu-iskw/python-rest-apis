# RESTful API in Python

[Performance Result with docker](./docs/performance_docker.md)

## Prerequisites
- Anaconda
- Docker
- docker-compose
- vegeta
    - `brew install vegeta`


## Commands
```
# Command to create, update and remove the conda environment.
make create-conda
make update-conda
make remove-conda

# lint and test
make lint
make test

# Build the docker images
make build-docker

# Run docker container with docker-compose.
make run-docker/tornado
make run-docker/uwsgi
```

## Motivation
I am looking for the best web framework and server in python for machine learning microservices.
I saw some articles that uWSGI's perormance is not good with high concurrencies.
So I want to make sure the performance of uWSGI and tornado by myself.

- A Performance Analysis of Python WSGI Servers: Part 2 | Blog | AppDynamics https://blog.appdynamics.com/engineering/a-performance-analysis-of-python-wsgi-servers-part-2/
- [Rewriting Uber Engineering: The Opportunities Microservices Provide \| Uber Engineering Blog](https://eng.uber.com/building-tincup/)
