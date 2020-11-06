## Annexe

All the modules we use for code re-formatting and testing are specified in 
[requirements-dev.txt](requirements.txt). Their configurations are defined in 
[pyproject.toml](pyproject.toml), [setup.cfg](setup.cfg) and 
[.pre-commit-config.yaml](.pre-commit-config.yaml).

### Code-formatting
In Arkhn's data team, we use [Black](https://black.readthedocs.io/en/stable/) and 
[Flake8](https://flake8.pycqa.org/en/latest/) to reformat our code. We also use 
[isort](https://pycqa.github.io/isort/) to re-organize our Python's imports.

### Testing
This repository implements tests in the `tests/` folder. To run them, we use 
[pytest](https://docs.pytest.org/en/stable/contents.html) and 
[Coverage.py](https://coverage.readthedocs.io/en/coverage-5.3/). To test the code, you can 
simply run `pytest` from the root of the repository. To add a coverage analysis, use 
`coverage run -m pytest; coverage report -m` instead. You can also add `coverage erase` at 
the end of the previous command in order to delete the files created by Coverage.py.

Alternatively, for a complete test of the package on a fresh environment, we use 
[tox](https://tox.readthedocs.io/en/latest/). To do so, simply run `tox` from the root of the
repository.

### pre-commit
We use [pre-commit](https://pre-commit.com/) to automatically run a variety of sanity checks 
and our code reformatting before each commit. To use it, after `pip install`ing it, simply
install it on this repository with `pre-commit install` from the root of the repository.

### Contributing
If you want to contribute to this repository, please make sure to have pre-commit installed 
on the repository to ensure proper code formatting and best practices before any commit. 

Furthermore, please run the tests before pushing anything to any branch of the repository.
