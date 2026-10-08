# SPDX-FileCopyrightText: Copyright (C) 2026 Nicolas Lamirault <nicolas.lamirault@gmail.com>
# SPDX-License-Identifier: Apache-2.0

BANNER = K O R T E X  /  W E B S I T E

SHELL = /bin/bash -o pipefail

NO_COLOR=\033[0m
OK_COLOR=\033[32;01m
ERROR_COLOR=\033[31;01m
INFO_COLOR=\033[36m
WHITE_COLOR=\033[1m

OK=[🟢]
KO=[🔴]
INFO=[🔵]

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo -e "$(OK_COLOR)      $(BANNER)$(NO_COLOR)"
	@echo "------------------------------------------------------------------"
	@echo ""
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make ${INFO_COLOR}<target>${NO_COLOR}\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  ${INFO_COLOR}%-16s${NO_COLOR} %s\n", $$1, $$2 } /^##@/ { printf "\n${WHITE_COLOR}%s${NO_COLOR}\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
	@echo ""

##@ Development

.PHONY: install
install: ## Install dependencies
	@echo -e "$(INFO)$(INFO_COLOR) Installing dependencies$(NO_COLOR)"
	bun install

.PHONY: dev
dev: ## Start the Astro dev server
	@echo -e "$(INFO)$(INFO_COLOR) Starting Astro dev server$(NO_COLOR)"
	bun run dev

.PHONY: build
build: tokens-check ## Build the static site into dist/
	@echo -e "$(INFO)$(INFO_COLOR) Building Astro site$(NO_COLOR)"
	bun run build

.PHONY: preview
preview: ## Preview the built site
	@echo -e "$(INFO)$(INFO_COLOR) Previewing built site$(NO_COLOR)"
	bun run preview

##@ Quality

.PHONY: check
check: tokens-check ## Run Astro type/content check
	@echo -e "$(INFO)$(INFO_COLOR) Running astro check$(NO_COLOR)"
	bun run check

##@ Design System

.PHONY: tokens
tokens: ## Regenerate src/styles/global.css tokens from DESIGN.md
	@echo -e "$(INFO)$(INFO_COLOR) Generating global.css tokens from DESIGN.md$(NO_COLOR)"
	python3 hack/gen-design-tokens.py

.PHONY: tokens-check
tokens-check: ## Verify global.css matches DESIGN.md (no drift)
	@echo -e "$(INFO)$(INFO_COLOR) Checking global.css is in sync with DESIGN.md$(NO_COLOR)"
	python3 hack/gen-design-tokens.py --check

##@ Deployment

.PHONY: deploy-dry
deploy-dry: build ## Validate the Worker + wrangler config without deploying
	@echo -e "$(INFO)$(INFO_COLOR) Validating Worker (dry run)$(NO_COLOR)"
	bunx wrangler deploy --dry-run

.PHONY: deploy
deploy: build ## Deploy to Cloudflare Workers
	@echo -e "$(INFO)$(INFO_COLOR) Deploying to Cloudflare Workers$(NO_COLOR)"
	bunx wrangler deploy

##@ Maintenance

.PHONY: clean
clean: ## Remove build artifacts
	@echo -e "$(INFO)$(INFO_COLOR) Removing build artifacts$(NO_COLOR)"
	rm -rf dist/ .astro/ .wrangler/ node_modules/.astro/
