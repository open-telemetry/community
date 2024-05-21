.PHONY: table-generation

table-generation:
	docker run --rm -v ${PWD}:/repo -w /repo python:3-alpine python ./scripts/update-sig-tables.py --install;


validate-sigs:
	docker run --rm -v ${PWD}:/repo -w /repo python:3-alpine python ./scripts/validate-sigs.py --install;

table-check:
	docker run --rm -v ${PWD}:/repo -w /repo python:3-alpine python ./scripts/update-sig-tables.py --install --check;
