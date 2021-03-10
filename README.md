# CODOC Python SDK
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=svadilfare_codoc-python&metric=coverage&token=87db581f3fdbed3f091a90ed187a1a0cad581529)](https://sonarcloud.io/dashboard?id=svadilfare_codoc-python)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=svadilfare_codoc-python&metric=security_rating&token=87db581f3fdbed3f091a90ed187a1a0cad581529)](https://sonarcloud.io/dashboard?id=svadilfare_codoc-python)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=svadilfare_codoc-python&metric=reliability_rating&token=87db581f3fdbed3f091a90ed187a1a0cad581529)](https://sonarcloud.io/dashboard?id=svadilfare_codoc-python)

This is the SDK for [Codoc](https://codoc.org/), that makes it possible to
upload architectural views of your python codebase directly to the
[Codoc](https://codoc.org/) interface.

## What is Codoc?
Codoc is the first Continuous Documentation tool.
It provides a revolutionary graph based interface,
that gives a powerful overview of any software system.
We are currently looking for [beta testers](https://codoc.org/signup/)

## Supported Version
We support python 3.6<

## Getting Started
Install the codoc SDK:

``` sh
pip3 install codoc
```


Then create a file i.e `codoc_views.py` in your root repository:

``` python
import os
from codoc import create_graph_from_module, publish
from codoc.filters import filter_only_classes
import my_package

graph = create_graph_from_module(my_package)

class_diagram = filter_only_classes(graph)

publish(
    graph_id="my_package-classdiagram",
    label="My super cool graph!",
    graph=class_diagram,
    api_key=os.getenv("CODOC_API_KEY")
)
```
