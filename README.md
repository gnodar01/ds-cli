# ds-cli

A CLI helper tool for [Distributed-Something](https://distributedscience.github.io/Distributed-Something/introduction.html)

## Development

### Setup Virtual Environment

Setup a python environment using the method of your choice.

Using the builtin `venv`:

    python -m venv dscli
    source dscli/bin/activate

Using `conda` (replace with any `python >= 3.8`):

    conda create -n dscli python=3.8
    conda activate dscli

Using whatever else you want, like [pyenv](https://github.com/pyenv/pyenv).

### Install dev tools

Install [Poetry](https://python-poetry.org/)

    curl -sSL https://install.python-poetry.org/ | python
    source ~/.poetry/env

Install [Nox](https://nox.thea.codes/en/stable/)

    pip install --user --upgrade nox

See [this post](https://medium.com/@cjolowicz/nox-is-a-part-of-your-global-developer-environment-like-poetry-pre-commit-pyenv-or-pipx-1cdeba9198bd) if you're curious as to why we don't install nox via Poetry.

Let Poetry install the rest from `pyproject.toml`

    poetry install

### Testing

[Coverage.py](https://coverage.readthedocs.io/en/7.2.2/) is used for test coverage, alongside [pytest](https://docs.pytest.org/en/7.2.x/), via the [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) plugin.

To run the tests directly, in you virtual environment, run `pytest --cov`.

To let nox run across multiple isolated environments, run `nox`.

To avoid nox recreating the virtual environments from scratch on each invocation, run `nox -r`.

Run a specific test with `nox -s tests -- tests/test_TESTNAME`.

### Static analysis

Autoformatting is performed with [Black](https://github.com/psf/black).

Run formatting with `nox -s black` or specify files/directors with `nox -s black -- file1 dir1 ...`.

Black auto-formatting is not run by default when running `nox` in isolation, it must be specified.

[Flake8](https://flake8.pycqa.org/en/latest/) is used for linting. Under the hood, it uses [pylint](https://www.pylint.org/), [pyflakes](https://github.com/PyCQA/pyflakes) for invalid python code (errors reported as `F`), [pycodestyle](https://github.com/pycqa/pycodestyle) for [PEP 8](https://peps.python.org/pep-0008/) style checking (`W` for warnings, `E` for errors), and [mccabe](https://github.com/PyCQA/mccabe) for code complexity (errors reported as `C`). Adherence to Black code style is performed via the [flake8-black](https://github.com/peterjc/flake8-black) plugin (erros reported as `BLK`). Import grouping and ordering is checked against the [Google styleguide](https://google.github.io/styleguide/pyguide.html?showone=Imports_formatting#313-imports-formatting) via the [flake8-import-order](https://github.com/PyCQA/flake8-import-order) plugin (errors reported as `I`). All of these are configured in the `.flake8` file.

Run linting with `nox -s lint` or specify files/directoriess with `nox -s lint -- file1 dir1 ...`.
