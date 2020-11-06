# Arkhn Data Team's Project Template

This repository is a template for Arkhn's data team Python projects.

All heavy data stuff must be inside a folder `/data/` and will be git-ignored.

To manage the documentation, you can use mkdocs. Its configuration file is `/mkdocs.yml`.

## Annexe
### Code-formatting
In Arkhn's data team, we use Black and Flake8 to reformat our code. Their configuration files 
are respectively `/pyproject.toml` and `/.flake8`. Additionally, we use isort to re-organize our 
imports. Its configuration file is `/.isort.cfg`.

### Testing
This repository implements tests in the `/tests/` folder. To run them, install pytest (e.g. with 
`pip install pytest`) and simply run the command `pytest` at the root of this repository.

### pre-commit
We use pre-commit to run a variety of sanity checks and our code
reformatting before each commit. To use it, download
pre-commit (e.g. with `pip install pre-commit`) and install it on this repository with
`pre-commit install` from the root of the repository. pre-commit's configuration file is 
`/.pre-commit-config.yaml`.

### Contributing
If you want to contribute to this repository, before any commit, please make sure you run the tests
(with pytest) and that you have installed pre-commit on this repository.
