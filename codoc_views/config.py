#!/usr/bin/env python3
from codoc import new_graph

from dotenv import load_dotenv

import codoc


def bootstrap(**kwargs):
    load_dotenv()
    return new_graph(codoc, **kwargs)
