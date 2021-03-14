#!/usr/bin/env python3
"""
The Command Line Interface for
the Codoc SDK.


Mainly used to publish your views to the webapp.
"""
import os
import fire
import codoc
from codoc.service.graph import create_graph_of_module

from codoc.service.finder.files import (
    get_all_codoc_files,
)

from codoc.service.finder.views import get_views_in_file, get_views_in_folder

NO_API_ERROR = """
API Key is not supplied.
Please set 'CODOC_API_KEY' as an environmental variable

Alternatively consult the documentation at https://codoc.org
"""


def publish(path="codoc_views"):
    """
    Publish all graphs in the current package
    """
    api_key = os.getenv("CODOC_API_KEY")
    if not api_key:
        return NO_API_ERROR
    graph = create_graph_of_module(codoc)

    files = get_all_codoc_files(path)
    views = [view for f in files for view in get_views_in_file(f)]
    resp = []
    for view in views:
        resp.append(f"Publishing {view.label}...")
        link = view(graph=graph, api_key=api_key)
        resp.append(f"published at {link}")

    return "\n".join(resp)


def list_views(path="codoc_views"):
    """
    returns a list of all the views found.
    """
    views = get_views_in_folder(path)
    if not views:
        return "No views found"
    sep = " - "
    return sep + ("\n" + sep).join(v.__name__ for v in views)


def list_files(path="codoc_views"):
    """
    returns a list of all the codoc related files found.
    """
    files = get_all_codoc_files(path)
    if not files:
        return "No files found"
    sep = " - "
    return sep + ("\n" + sep).join(f.name for f in files)


def _main():
    fire.Fire()


if __name__ == "__main__":
    _main()
