.PHONY: proto build all run help
SHELL = /bin/bash
CMD = python

GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
CYAN   := $(shell tput -Txterm setaf 6)
RESET  := $(shell tput -Txterm sgr0)


all: help



## Build :
build:
	@mkdir -p gen
	@mkdir -p build
	@python setup.py build
	@python -m grpc_tools.protoc -I ./proto \
	  --proto_path=proto/ \
	  --python_out=gen/ \
	  --grpc_python_out=gen/ \
	  --pyi_out=gen/ \
	  ./proto/*


## Run:
run: build ## Run project
	@python main.py


## Help:
help: ## Show this help.
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} { \
			if (/^[a-zA-Z_-]+:.*?##.*$$/) {printf "    ${YELLOW}%-20s${GREEN}%s${RESET}\n", $$1, $$2} \
			else if (/^## .*$$/) {printf "  ${CYAN}%s${RESET}\n", substr($$1,4)} \
			}' $(MAKEFILE_LIST)


