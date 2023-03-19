from ds_cli import dscli


def test_hello_succeeds(runner):
    result = runner.invoke(dscli.hello)
    assert result.exit_code == 0
