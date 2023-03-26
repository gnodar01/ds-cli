import click.testing
import pytest


@pytest.fixture(scope="function")
def runner() -> click.testing.CliRunner:
    return click.testing.CliRunner(mix_stderr=False)


@pytest.fixture(scope="function")
def echo_runner() -> click.testing.CliRunner:
    return click.testing.CliRunner(echo_stdin=True)
