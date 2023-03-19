import nox


nox.options.sessions = "lint", "tests"


locations = "src", "tests", "noxfile.py"


@nox.session(python=["3.8"])
def black(session):
    # override with nox -s black -- arg1 arg2 ...
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python=["3.8"])
def lint(session):
    # override with nox -s lint -- arg1 arg2 ...
    args = session.posargs or locations
    session.install("flake8", "flake8-black", "flake8-import-order", "flake8-bugbear")
    session.run("flake8", *args)


@nox.session(python=["3.8"])
def tests(session):
    # pass along args to pytest
    args = session.posargs or ["--cov"]
    # poetry is not part of the environment created by Nox,
    # so we specify external to void warnings about external
    # commands leaking into the isolated test environments
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)
