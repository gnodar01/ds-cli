import click.testing
import pytest


@pytest.fixture(scope="function")
def runner():
    return click.testing.CliRunner()
