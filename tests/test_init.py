from pathlib import Path
from typing import Any

from click.testing import CliRunner
import pytest
from rich.prompt import Confirm
from rich_click import Abort

from ds_reify import dsreify
from ds_reify.commands import init


################
# Direct tests #
################


def test_overwrite_contents(tmp_path: Path) -> None:
    project_dir = tmp_path / "test_project"
    project_dir.mkdir()
    (project_dir / "test_file").touch()
    (project_dir / "test_dir").mkdir()
    (project_dir / "test_dir" / "test_nexted_file").touch()
    init.overwrite_contents(str(project_dir))
    assert not list(project_dir.iterdir())


def test_create_nonexistent_project_dir(tmp_path: Path) -> None:
    project_dir = tmp_path / "test_project"
    assert not project_dir.exists()
    init.create_project_dir(str(project_dir))
    assert project_dir.exists()
    project_dir.rmdir()


def test_create_project_dir_aborted(tmp_path: Path, monkeypatch: Any) -> None:
    project_name = "test_project"
    project_dir = tmp_path / project_name
    project_dir.mkdir()
    (project_dir / "test_file").touch()
    (project_dir / "test_dir").mkdir()
    (project_dir / "test_dir" / "test_nexted_file").touch()
    monkeypatch.setattr(Confirm, "ask", lambda prompt, *args, **kwargs: False)
    with pytest.raises(Abort) as exc_info:
        init.create_project_dir(str(project_dir))
    assert exc_info.typename == "Abort"


########################
# CLI invocation tests #
########################


def test_create_existing_project_dir(runner: CliRunner, tmp_path: Path) -> None:
    project_name = "test_project"
    project_dir = tmp_path / project_name
    project_dir.mkdir()
    (project_dir / "test_file").touch()
    (project_dir / "test_dir").mkdir()
    (project_dir / "test_dir" / "test_nexted_file").touch()
    inputs = [project_name, str(project_dir), "y", ""]
    runner.invoke(dsreify.init, input="\n".join(inputs))
    assert project_dir.exists()
    assert not list(project_dir.iterdir())


def test_abort_existing_project_dir(runner: CliRunner, tmp_path: Path) -> None:
    project_name = "test_project"
    project_dir = tmp_path / project_name
    project_dir.mkdir()
    (project_dir / "test_file").touch()
    (project_dir / "test_dir").mkdir()
    (project_dir / "test_dir" / "test_nexted_file").touch()
    inputs = [project_name, str(project_dir), "n", ""]
    result = runner.invoke(dsreify.init, input="\n".join(inputs))
    assert result.exit_code == 1
    assert "Aborted" in result.output
    assert project_dir.exists()
    assert len(list(project_dir.iterdir())) == 2


def test_init_no_project_name_err(runner: CliRunner) -> None:
    inputs = ["", ""]
    result = runner.invoke(dsreify.init, input="\n".join(inputs))
    assert result.exit_code == 1
    assert "Project Name" in result.output


def test_init_succeeds(runner: CliRunner, tmp_path: Path) -> None:
    project_dir = tmp_path / "test_project"
    inputs = ["test_project", str(project_dir), ""]
    result = runner.invoke(dsreify.init, input="\n".join(inputs))
    assert result.exit_code == 0
