import click.testing

from ds_cli import dscli

def test_main_succeeds():
    runner = click.testing.CliRunner()
    result = runner.invoke(dscli.main())
    assert result.exit_code == 0
