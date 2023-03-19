import pytest
import click.testing

from ds_cli import dscli


@pytest.fixture(scope='function')
def runner():
    return click.testing.CliRunner()

def test_main_succeeds(runner):
    result = runner.invoke(dscli.main)
    assert result.exit_code == 0
