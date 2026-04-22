# All documents to be used in spell check.
ALL_DOCS := $(shell find . -type f -name '*.md' -not -path './.github/*' -not -path './node_modules/*' | sort)

# This is needed to make the /repo paths below work in Windows Git Bash
export MSYS_NO_PATHCONV=1

.PHONY: generate
generate:
	docker run --rm -v ${PWD}:/repo -w /repo python:3-alpine python ./scripts/update-sig-tables.py --install;
	docker run --rm -v ${PWD}:/repo -w /repo python:3-alpine python ./scripts/update-community-members.py --install;

.PHONY: validate-sigs
validate-sigs:
	docker run --rm -v ${PWD}:/repo -w /repo python:3-alpine python ./scripts/validate-workstreams.py --install;

.PHONY: check-generate
check-generate:
	docker run --rm -v ${PWD}:/repo -w /repo python:3-alpine python ./scripts/update-sig-tables.py --install --check;
	docker run --rm -v ${PWD}:/repo -w /repo python:3-alpine python ./scripts/update-community-members.py --install --check;

.PHONY: markdown-link-check
markdown-link-check:
	docker run --rm \
		--mount 'type=bind,source=$(PWD),target=/home/repo' \
		-e GITHUB_TOKEN \
		lycheeverse/lychee:sha-8222559@sha256:6f49010cc46543af3b765f19d5319c0cdd4e8415d7596e1b401d5b4cec29c799 \
		--config home/repo/.lychee.toml \
		--root-dir /home/repo \
		--verbose \
		home/repo
