# Arkhn Data Team's Project Template

This repository is a template for Arkhn's data team Python projects.

All heavy data stuff must be inside a folder `/data/` and will be git-ignored.


## Annexe
### Code-formatting
In Arkhn's data team, we use Black to reformat our code. Black's configuration file is 
`/pyproject.toml`. The only notable parameter is that we use `--line-length=100`.

We also use Flake8 to reformat our code. Flake8's configuration file is `/.flake8`.
The only notable parameter is that we use `--max-line-length=100`.

### Testing
This repository implements tests in the `/tests/` folder. To run these tests, install `pytest`
and simply run the command `pytest` at the root of this repository.

### Contributing
If you want to contribute to this repository, make sure you run the tests (running the command
`pytest`) before pushing anything.

Furthermore, we use `pre-commit` to run a variety of sanity checks and code
reformatting before each commit. Therefore, please install
`pre-commit` (e.g. with `pip install pre-commit`) and install it on this repository with
`pre-commit install` at the root of the repository. Then, `pre-commit` will run its checks
before each commit. `pre-commit`'s configuration file is `/.pre-commit-config.yaml`.