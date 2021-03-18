# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["TestGetChildrenOfFilter.test_matches_snapshot[Exclude dependencies] 1"] = (
    ["ClassB", "FuncA", "ModuleB"],
    [("ClassB", "FuncA"), ("FuncA", "ClassB")],
)

snapshots["TestGetChildrenOfFilter.test_matches_snapshot[Include dependencies] 1"] = (
    ["ClassA", "ClassB", "FuncA", "FuncB", "ModuleA", "ModuleB"],
    [
        ("ClassA", "ClassB"),
        ("ClassA", "FuncA"),
        ("ClassB", "ClassA"),
        ("ClassB", "FuncA"),
        ("FuncA", "ClassB"),
        ("FuncA", "FuncB"),
        ("FuncA", "ModuleA"),
        ("ModuleA", "FuncA"),
        ("ModuleA", "ModuleB"),
    ],
)

snapshots["test_matches_snapshot[class_diagram_filter] 1"] = (
    ["ClassA", "ClassB"],
    [("ClassA", "ClassB"), ("ClassB", "ClassA")],
)

snapshots["test_matches_snapshot[exclude_classes] 1"] = (
    ["FuncA", "FuncB", "ModuleA", "ModuleB"],
    [
        ("FuncA", "FuncB"),
        ("FuncA", "ModuleA"),
        ("ModuleA", "FuncA"),
        ("ModuleA", "ModuleB"),
    ],
)

snapshots["test_matches_snapshot[exclude_functions] 1"] = (
    ["ClassA", "ClassB", "ModuleA", "ModuleB"],
    [
        ("ClassA", "ClassB"),
        ("ClassA", "ModuleA"),
        ("ClassB", "ClassA"),
        ("ModuleA", "ModuleB"),
    ],
)

snapshots["test_matches_snapshot[exclude_modules] 1"] = (
    ["ClassA", "ClassB", "FuncA", "FuncB"],
    [
        ("ClassA", "ClassB"),
        ("ClassA", "FuncA"),
        ("ClassB", "ClassA"),
        ("ClassB", "FuncA"),
        ("FuncA", "ClassB"),
        ("FuncA", "FuncB"),
    ],
)
