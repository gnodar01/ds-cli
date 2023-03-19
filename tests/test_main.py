from click.testing import CliRunner

from ds_cli import dscli


def test_main_succeeds(runner: CliRunner) -> None:
    result = runner.invoke(dscli.main)
    assert result.exit_code == 0
