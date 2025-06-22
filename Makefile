# All documents to be used in spell check.
ALL_DOCS := $(shell find . -type f -name '*.md' -not -path './.github/*' -not -path './node_modules/*' | sort)

# This is needed to make the /repo paths below work in Windows Git Bash
export MSYS_NO_PATHCONV=1

.PHONY: table-generation
table-generation:
	docker run --rm -v ${PWD}:/repo -w /repo python:3-alpine python ./scripts/update-sig-tables.py --install;

validate-sigs:
	docker run --rm -v ${PWD}:/repo -w /repo python:3-alpine python ./scripts/validate-sigs.py --install;

table-check:
	docker run --rm -v ${PWD}:/repo -w /repo python:3-alpine python ./scripts/update-sig-tables.py --install --check;

.PHONY: markdown-link-check
markdown-link-check:
	docker run --rm \
		--mount 'type=bind,source=$(PWD),target=/home/repo' \
		lycheeverse/lychee:sha-639c74e@sha256:ce2e490d25e886fb0b4b859feaea78bf0e36b7ce542c5e0393ff91b7e28517ad \
		--config home/repo/.lychee.toml \
		--root-dir /home/repo \
		--verbose \
		home/repo
