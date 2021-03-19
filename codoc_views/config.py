#!/usr/bin/env python3
from codoc.service.graph import create_graph_of_module

import codoc


def bootstrap():
    return create_graph_of_module(codoc)
