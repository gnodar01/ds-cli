from click.testing import CliRunner

from ds_reify import dsreify


def test_init_succeeds(runner: CliRunner) -> None:
    inputs = ["test_project", "blue"]
    result = runner.invoke(dsreify.init, input="\n".join(inputs))
    assert result.exit_code == 0
