from ds_cli import dscli


def test_main_succeeds(runner):
    result = runner.invoke(dscli.main)
    assert result.exit_code == 0
