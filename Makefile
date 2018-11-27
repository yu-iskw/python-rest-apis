NAME = python-rest-apis

BASE_DOCKER_IMAGE := yuiskw/$(NAME)


create-conda:
	conda env create -f environment.yml -n $(NAME)

update-conda:
	conda env update -f environment.yml -n $(NAME)

remove-conda:
	conda env remove -y -n $(NAME)

test:
	pytest -v ./tests

lint:
	flake8

build-docker:: build-docker/uwsgi

build-docker/%:
	docker build --rm -f docker/Dockerfile.$* -t $(BASE_DOCKER_IMAGE)-$*:dev .

run-docker/%:
	docker-compose -f docker-compose.$*.yml up
