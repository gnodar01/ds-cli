from click.testing import CliRunner

from ds_reify import dsreify


def test_hello_succeeds(runner: CliRunner) -> None:
    result = runner.invoke(dsreify.hello)
    assert result.exit_code == 0


def test_hello_world_succeeds(runner: CliRunner) -> None:
    result = runner.invoke(dsreify.hello, ["--say=world"])
    assert result.exit_code == 0
    assert "world" in result.output
