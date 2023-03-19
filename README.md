# ds-cli

A CLI helper tool for [Distributed-Something](https://distributedscience.github.io/Distributed-Something/introduction.html)

### Development

#### Setup Virtual Environment

Setup a python environment using the method of your choice.

Using the builtin `venv`:

    python -m venv dscli
    source dscli/bin/activate

Using `conda` (replace with any `python >= 3.8`):

    conda create -n dscli python=3.8
    conda activate dscli

Using whatever else you want, like [pyenv](https://github.com/pyenv/pyenv).

#### Install dev tools

Install [Poetry](https://python-poetry.org/)

    curl -sSL https://install.python-poetry.org/ | python
    source ~/.poetry/env

Install [Nox](https://nox.thea.codes/en/stable/)

    pip install --user --upgrade nox

See [this post](https://medium.com/@cjolowicz/nox-is-a-part-of-your-global-developer-environment-like-poetry-pre-commit-pyenv-or-pipx-1cdeba9198bd) if you're curious as to why we don't install nox via Poetry.

Let Poetry install the rest from `pyproject.toml`

    poetry install
