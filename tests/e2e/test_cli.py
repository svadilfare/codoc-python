#!/usr/bin/env python3
import pytest

from codoc.entrypoints.cli import (
    CliHandler,
)


def test_list_views(cli):
    assert len(cli.list_views().split("\n")) == 2


@pytest.fixture
def cli(tmp_path, mocker, codoc_view_file_content):
    f = tmp_path / "codoc_domain_model.py"
    f.write_text(codoc_view_file_content)
    return CliHandler(path=tmp_path)
