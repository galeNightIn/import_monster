PACKAGES="src"

all: install black

black:
	@black ${PACKAGES}

clean:
	@rm -rf `find . -name __pycache__`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -f `find . -type f -name '*~' `
	@rm -f `find . -type f -name '.*~' `
	@rm -f `find . -type f -name '@*' `
	@rm -f `find . -type f -name '#*#' `
	@rm -f `find . -type f -name '*.orig' `
	@rm -f `find . -type f -name '*.rej' `
	@rm -rf `find . -type d -name '.pytest_cache' `
	@rm -f .coverage
	@rm -rf htmlcov
	@rm -rf build
	@rm -rf cover
	@python setup.py clean
	@rm -rf .tox
	@rm -f .develop
	@rm -f .flake

install:
	@pip install -r requirements.txt

install-dev:
	@pip install -r requirements_dev.txt

install-test:
	@pip install -r requirements_test.txt
	@pip install -e .

install-all: install-dev install-test

pytest:
	@pytest
