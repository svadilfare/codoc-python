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
    ["Exception", "FuncA", "FuncB", "ModuleA", "ModuleB"],
    [
        ("FuncA", "FuncB"),
        ("FuncA", "ModuleA"),
        ("ModuleA", "FuncA"),
        ("ModuleA", "ModuleB"),
    ],
)

snapshots["test_matches_snapshot[exclude_exceptions] 1"] = (
    ["ClassA", "ClassB", "FuncA", "FuncB", "ModuleA", "ModuleB"],
    [
        ("ClassA", "ClassB"),
        ("ClassA", "FuncA"),
        ("ClassA", "ModuleA"),
        ("ClassB", "ClassA"),
        ("ClassB", "FuncA"),
        ("FuncA", "ClassB"),
        ("FuncA", "FuncB"),
        ("FuncA", "ModuleA"),
        ("ModuleA", "FuncA"),
        ("ModuleA", "ModuleB"),
    ],
)

snapshots["test_matches_snapshot[exclude_functions] 1"] = (
    ["ClassA", "ClassB", "Exception", "ModuleA", "ModuleB"],
    [
        ("ClassA", "ClassB"),
        ("ClassA", "Exception"),
        ("ClassA", "ModuleA"),
        ("ClassB", "ClassA"),
        ("ModuleA", "ModuleB"),
    ],
)

snapshots["test_matches_snapshot[exclude_modules] 1"] = (
    ["ClassA", "ClassB", "Exception", "FuncA", "FuncB"],
    [
        ("ClassA", "ClassB"),
        ("ClassA", "Exception"),
        ("ClassA", "FuncA"),
        ("ClassB", "ClassA"),
        ("ClassB", "FuncA"),
        ("FuncA", "ClassB"),
        ("FuncA", "FuncB"),
    ],
)

snapshots["test_matches_snapshot[include_only_classes] 1"] = (
    ["ClassA", "ClassB"],
    [("ClassA", "ClassB"), ("ClassB", "ClassA")],
)

snapshots["test_matches_snapshot[include_only_exceptions] 1"] = (["Exception"], [])

snapshots["test_matches_snapshot[include_only_functions] 1"] = (
    ["FuncA", "FuncB"],
    [("FuncA", "FuncB")],
)

snapshots["test_matches_snapshot[include_only_modules] 1"] = (
    ["ModuleA", "ModuleB"],
    [("ModuleA", "ModuleB")],
)
