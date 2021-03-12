#!/usr/bin/env python3
from codoc.service.finder.files import (
    get_all_files,
    get_all_codoc_files,
    get_all_python_files,
)
from codoc.service.finder.views import (
    get_views_in_file,
)


CONTENT = "test()"


def test_get_all_files__returns_file(tmp_path):
    folder = tmp_path / "codoc_views"
    folder.mkdir()
    codoc_file = folder / "view_domain_model.py"
    codoc_file.write_text(CONTENT)

    assert codoc_file in get_all_files(tmp_path)


def test_get_all_files__returns_file_in_sub_dir(tmp_path):
    folder = tmp_path / "codoc_views"
    folder.mkdir()
    sub_folder = folder / "domain"
    sub_folder.mkdir()

    f = sub_folder / "view.py"
    f.write_text(CONTENT)

    assert f in get_all_files(folder)


def test_get_all_python_files(tmp_path):
    folder = tmp_path / "codoc_views"
    folder.mkdir()
    f = folder / "view_domain_model.py"
    f.write_text(CONTENT)

    assert f in get_all_python_files(tmp_path)


def test_get_all_python_files__ignores_non_py_files(tmp_path):
    folder = tmp_path / "codoc_views"
    folder.mkdir()
    f = folder / "view_domain_model.txt"
    f.write_text(CONTENT)

    assert not get_all_python_files(tmp_path)


def test_get_all_codoc_files__ignores_non_py_files(tmp_path):
    folder = tmp_path / "codoc_views"
    folder.mkdir()
    f = folder / "view_domain_model.txt"
    f.write_text(CONTENT)

    assert not get_all_codoc_files(tmp_path)


def test_get_all_codoc_files__ignores_non_codoc_files(tmp_path):
    folder = tmp_path / "codoc_views"
    folder.mkdir()
    f = folder / "test_domain_model.py"
    f.write_text(CONTENT)

    assert not get_all_codoc_files(tmp_path)


def test_get_all_codoc_files(tmp_path):
    folder = tmp_path / "codoc_views"
    folder.mkdir()
    f = folder / "codoc_domain_model.py"
    f.write_text(CONTENT)

    assert f in get_all_codoc_files(tmp_path)


def test_get_views_in_file(snapshot, tmp_path, codoc_view_file_content):
    f = tmp_path / "codoc_domain_model.py"
    f.write_text(codoc_view_file_content)
    views = get_views_in_file(f)

    snapshot.assert_match({view.__name__ for view in views})
