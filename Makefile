# SPDX-FileCopyrightText: Copyright (C) 2026 Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

BANNER = P R O J E C T  N A M E

SHELL = /bin/bash -o pipefail

DIR = $(shell pwd)

# Colors for terminal output
NO_COLOR=\033[0m
OK_COLOR=\033[32;01m
ERROR_COLOR=\033[31;01m
WARN_COLOR=\033[33;01m
INFO_COLOR=\033[36m
WHITE_COLOR=\033[1m
MAKE_COLOR=\033[33;01m%-20s\033[0m

.DEFAULT_GOAL := help

# Define common messages
# OK=[✅]
# KO=[🔴]
# WARN=[⚠️]
# INFO=[🔵]
OK=[🟢]
KO=[🔴]
WARN=[🟠]
INFO=[🔵]


.PHONY: help
help:
	@echo -e "$(OK_COLOR)      $(BANNER)$(NO_COLOR)"
	@echo "------------------------------------------------------------------"
	@echo ""
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make ${INFO_COLOR}<target>${NO_COLOR}\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  ${INFO_COLOR}%-25s${NO_COLOR} %s\n", $$1, $$2 } /^##@/ { printf "\n${WHITE_COLOR}%s${NO_COLOR}\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
	@echo ""

guard-%:
	@if [ "${${*}}" = "" ]; then \
		echo -e "$(ERROR_COLOR)Environment variable $* not set$(NO_COLOR)"; \
		exit 1; \
	fi

check-%:
	@if $$(hash $* 2> /dev/null); then \
		echo -e "$(OK_COLOR)$(OK)$(NO_COLOR) $*"; \
	else \
		echo -e "$(ERROR_COLOR)$(KO)$(NO_COLOR) $*"; \
	fi

.PHONY: kb
kb: ## Rebuild knowledge-base entity pages from the wiki graph
	@echo -e "$(INFO)$(INFO_COLOR)[KB] Building knowledge base $(NO_COLOR)"
	@python3 scripts/build_knowledge_base.py

.PHONY: site-build
site-build: ## Build the static wiki website into website/public
	@echo -e "$(INFO)$(INFO_COLOR)[Site] Build $(NO_COLOR)"
	@./website/build.sh

.PHONY: site-preview
site-preview: ## Preview the wiki website locally (localhost:4321)
	@echo -e "$(INFO)$(INFO_COLOR)[Site] Preview $(NO_COLOR)"
	@./website/build.sh --serve

# wrangler is run on-demand via npx (not a project dependency). Pin the major
# to keep deploys reproducible.
WRANGLER = npx --yes wrangler@4

.PHONY: site-serve
site-serve: site-build ## Serve the built site through the Cloudflare Worker locally (wrangler dev)
	@echo -e "$(INFO)$(INFO_COLOR)[Site] Serving via wrangler dev $(NO_COLOR)"
	@cd website && $(WRANGLER) dev

.PHONY: site-deploy
site-deploy: site-build ## Deploy the site to Cloudflare Workers (wrangler deploy)
	@echo -e "$(INFO)$(INFO_COLOR)[Site] Deploying to Cloudflare $(NO_COLOR)"
	@cd website && $(WRANGLER) deploy

.PHONY: clean
clean: ## Clean project
	@echo -e "$(INFO)$(INFO_COLOR)[Clean] Processing $(NO_COLOR)"
	@rm -rf website/dist website/.astro website/.wrangler
