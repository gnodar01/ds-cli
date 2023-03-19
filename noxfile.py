import tempfile

import nox


nox.options.sessions = "lint", "tests"


locations = "src", "tests", "noxfile.py"


def install_with_constraints(session, *args, **kwargs):
    """Install packages constrained by poetry.lock."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--with",
            "dev,test",
            # "--format=requirements.txt",
            "--format=constraints.txt",
            "--without-hashes",
            "--output",
            requirements.name,
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session(python=["3.8"])
def black(session):
    # override with nox -s black -- arg1 arg2 ...
    args = session.posargs or locations
    install_with_constraints(session, "black")
    session.run("black", *args)


@nox.session(python=["3.8"])
def lint(session):
    # override with nox -s lint -- arg1 arg2 ...
    args = session.posargs or locations
    install_with_constraints(
        session,
        "flake8",
        "flake8-black",
        "flake8-import-order",
        "flake8-bugbear",
        "flake8-bandit",
    )
    session.run("flake8", *args)


@nox.session(python=["3.8"])
def safety(session):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--with",
            "dev,test",
            "--format=requirements.txt",
            "--without-hashes",
            "--output",
            requirements.name,
            external=True,
        )
        install_with_constraints(session, "safety")
        session.run("safety", "check", "--file", requirements.name, "--full-report")


@nox.session(python=["3.8"])
def tests(session):
    # pass along args to pytest
    args = session.posargs or ["--cov"]
    # poetry is not part of the environment created by Nox,
    # so we specify external to void warnings about external
    # commands leaking into the isolated test environments
    session.run("poetry", "install", "--without", "dev", external=True)
    install_with_constraints(
        session, "coverage[toml]", "pytest", "pytest-cov", "pytest-mock"
    )
    session.run("pytest", *args)
