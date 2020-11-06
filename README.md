# Arkhn Data Team's Project Template

This repository is a template for Arkhn's data team Python projects.

All heavy data stuff must be inside a folder `/data/` and will be git-ignored.

## Annexe

All the modules we use for code re-formatting and testing are specified in 
`/requirements-dev.txt`. Their configurations are defined in `/pyproject.toml`, `/setup.cfg` 
and `/.pre-commit-config.yaml`.

### Code-formatting
In Arkhn's data team, we use Black and Flake8 to reformat our code. We also use isort to 
re-organize our Python's imports.

### Testing
This repository implements tests in the `/tests/` folder. To run them, we use pytest and 
Coverage.py. To test the code, you can simply run `pytest` from the root of the repository; to
add a coverage analysis, use `coverage run -m pytest; coverage report -m` instead.

Alternatively, for a complete test of the package, you can use tox to run the test in 
a fresh environment. To do so, simply run `tox` from the root of the repository.

### pre-commit
We use pre-commit to automatically run a variety of sanity checks and our code
reformatting before each commit. To use it, after `pip install`ing it, simply install it on this
repository with `pre-commit install` from the root of the repository.

### Contributing
If you want to contribute to this repository, please make sure to have pre-commit installed 
on the repository to ensure proper code formatting and best practices before any commit. 

Furthermore, please run the tests before pushing anything to a branch of the repository.
