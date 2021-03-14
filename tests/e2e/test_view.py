#!/usr/bin/env python3
from codoc.service.finder.views import (
    get_views_in_folder,
)


def test_views_publish_graphs(
    snapshot, api_key, generic_graph, mocker, tmp_path, codoc_view_file_content
):
    mock_publish = mocker.Mock()
    f = tmp_path / "codoc_domain_model.py"
    f.write_text(codoc_view_file_content)
    views = get_views_in_folder(tmp_path)

    for view in views:
        view(generic_graph, api_key=api_key, publish_func=mock_publish)

    assert mock_publish.call_count == 2
