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
	@if ! npm ls markdown-link-check; then npm install; fi
	find . -type f \
		-name '*.md' \
		-not -path './node_modules/*' \
		-not -path './elections/*/governance-committee-election.md' \
		-not -path './elections/*/governance-committee-candidates.md' \
		| xargs .github/scripts/markdown-link-check-with-retry.sh

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
