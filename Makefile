APP_NAME=`cat project.name`
PROJECT_PY_FILES=`cd src && find . -type f -regex "^.*.py" -not -path ./${DEST_DIRECTORY}/\* -not -path ./${PROTO_DIRECTORY}/\*

all:  build up restart down logs pre-commit ipython bash

.PHONY: build
build:
	@#@ build docker image
	@docker-compose build
	@echo Done build


.PHONY: up
up:
	@#@ Run docker-compose up
	@docker-compose up -d
	@echo Done up

.PHONY: restart
restart:
	@#@ Runs docker-compose down
	@docker-compose restart
	@echo Done restart

.PHONY: down
down:
	@#@ Runs docker-compose down
	@docker-compose down -v
	@echo Done down

.PHONY: logs
logs:
	@#@ Runs logs from docker
	@docker-compose logs -f

.PHONY: pre-commit
pre-commit:
	@pre-commit run --all-files

.PHONY: ipython
ipython:
	@docker-compose run ${APP_NAME} ipython

.PHONY: bash
bash:
	@docker-compose run ${APP_NAME} ipython
