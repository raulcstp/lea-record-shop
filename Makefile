_flake8:
	@flake8 --statistics --show-source app/

_black:
	@black --check app/

_black_fix:
	@black app/

test:
	@pytest -x tests/

_pip_install_requirements:
	pip install -r requirements.txt

_pip_install_requirements_dev:
	pip install -r requirements_dev.txt

_pre_commit_install:
	pre-commit install

lint: _flake8 _black  ## Check code lint
format-code: _black_fix ## Format code
install_dev: _pip_install_requirements _pip_install_requirements_dev _pre_commit_install ## Project installation
install_prod: _pip_install_requirements