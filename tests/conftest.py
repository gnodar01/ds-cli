import click.testing
import pytest


@pytest.fixture(scope="function")
def runner() -> click.testing.CliRunner:
    return click.testing.CliRunner()
