from click.testing import CliRunner

from dscli import dscli


def test_hello_succeeds(runner: CliRunner) -> None:
    result = runner.invoke(dscli.hello)
    assert result.exit_code == 0


def test_hello_world_succeeds(runner: CliRunner) -> None:
    result = runner.invoke(dscli.hello, ["--say=world"])
    assert result.exit_code == 0
    assert "world" in result.output
