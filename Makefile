APP_NAME=`cat project.name`
DCE = docker-compose exec ${APP_NAME}
PROJECT_PY_FILES=`cd src && find . -type f -regex "^.*.py" -not -path ./${DEST_DIRECTORY}/\* -not -path ./${PROTO_DIRECTORY}/\* -not -path ./shared/\*`

LOCAL_IMAGE = ${APP_NAME}-service

all:  build up


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

.PHONY: bash
bash:
	@#@ Runs bash in container
	@${DCE} bash

.PHONY: pre-commit
pre-commit:
	@pre-commit run --all-files
