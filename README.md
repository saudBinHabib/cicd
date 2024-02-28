# FastAPI Example

## Getting Started

To set up your local development environment, please use a fresh virtual environment

    `python -m venv .venv`

then run:

    `source .venv/bin/activate`
    `pip install -r requirements/dev.txt`

The upper command will activate the fresh virtual environment, and the lower command will install all the requirements.

### Testing

We use `pytest` as test framework. To execute the tests, please run

    `pytest tests`

To run the tests with coverage information, please use

    `pytest tests --cov=src --cov-report=html --cov-report=term`

and have a look at the `htmlcov` folder, after the tests are done.

### Notebooks

You can test, and debug the api's and models using notebooks, in the notebook directory.

### Contributions

Before contributing, please set up the pre-commit hooks to reduce errors and ensure consistency

    `pre-commit install`
    `pre-commit run --all-files

`

If you run into any issues, you can remove the hooks again with `pre-commit uninstall`.

## Contact

Saud Bin Habib (saud.habib@alexanderthamm.com)

## License

© at
