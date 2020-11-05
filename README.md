# General Git project template

Custom template for Git projects. 

All heavy data stuff must be inside a folder `/data/` and will be Git-ignored.

## Black
This repository implements Black to re-format its code. Black's configuration file is 
`/.pyproject.toml`.

## Flake8
This repository implements Flake9 to re-format its code. Flake8's configuration file is `/.flake8`.

## Pre-commit
In this repository, pre-commit is available. To use it, you must install it, running `pre-commit
 install` at the root of this repository. Pre-commit configuration file is `
 /.pre-commit-config.yaml`. In addition to a few sanity checks, this pre-commit set-up implements 
 Black's and Flake8's reformatting.
