.PHONY: table-generation

table-generation:
	@if command -v python3 >/dev/null 2>&1; then \
		echo "Python3 is installed. Running the script locally:"; \
		python3 ./scripts/update-sig-tables.py; \
	else \
		echo "Python3 is not installed. Running Docker container:"; \
		docker run --rm -v ${PWD}:/repo -w /repo python:3-alpine python ./scripts/update-sig-tables.py --install; \
	fi


validate-sigs:
	@if command -v python3 >/dev/null 2>&1; then \
		echo "Python3 is installed. Running the script locally:"; \
		python3 ./scripts/validate-sigs.py; \
	else \
		echo "Python3 is not installed. Running Docker container:"; \
		docker run --rm -v ${PWD}:/repo -w /repo python:3-alpine python ./scripts/validate-sigs.py --install; \
	fi