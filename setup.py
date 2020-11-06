from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().split()

setup(
    name="arkhn-",  # e.g. arkhn-pyckaxe
    version="0.0.1",
    author="Arkhn's Data Team",
    author_email="data@arkhn.com",
    description="",  # e.g. "Arkhn's Pyckaxe package: a toolbox for Pypa."
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",  # e.g. "https://github.com/arkhn/pyckaxe"
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache :: 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
