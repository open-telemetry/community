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
		lycheeverse/lychee@sha256:2e3786630482c41f9f2dd081e06d7da1c36d66996e8cf6573409b8bc418d48c4 \
		--config home/repo/.lychee.toml \
		--root-dir /home/repo \
		--verbose \
		home/repo

# This target runs markdown-toc on all files that contain
# a pair of comments <!-- toc --> and <!-- tocstop -->.
.PHONY: markdown-toc
markdown-toc:
	@if ! npm ls markdown-toc; then npm install; fi
	@for f in $(ALL_DOCS); do \
		if grep -q '<!-- tocstop -->' $$f; then \
			echo markdown-toc: processing $$f; \
				npx --no -- markdown-toc --no-first-h1 --no-stripHeadingTags -i $$f || exit 1; \
		else \
			echo markdown-toc: no TOC markers, skipping $$f; \
		fi; \
	done

markdown-toc-check: markdown-toc
	git diff --exit-code ':*.md' || (echo 'Generated markdown Table of Contents is out of date, please run "make markdown-toc" and commit the changes in this PR.' && exit 1)
