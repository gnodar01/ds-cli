import pytest
import click.testing

@pytest.fixture(scope='function')
def runner():
    return click.testing.CliRunner()
