from click.testing import CliRunner

from ds_reify import dsreify


def test_main_succeeds(runner: CliRunner) -> None:
    result = runner.invoke(dsreify.main)
    assert result.exit_code == 0
