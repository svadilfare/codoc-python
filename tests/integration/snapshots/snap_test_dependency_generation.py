# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_get_dependency_edges_match_snapshot[With external nodes-Class] 1"] = [
    ("examples/Animal/NodeType.CLASS", "builtins/str/NodeType.CLASS"),
    ("examples/Animal/NodeType.CLASS", "dataclasses/dataclass/NodeType.FUNCTION"),
    ("examples/Animal/NodeType.CLASS", "examples/Animal/NodeType.CLASS"),
    ("examples/Animal/NodeType.CLASS", "examples/AnimalType/NodeType.CLASS"),
    ("examples/Animal/NodeType.CLASS", "typing/List/NodeType.CLASS"),
]

snapshots[
    "test_get_dependency_edges_match_snapshot[With external nodes-Function] 1"
] = [
    ("examples/random_function/NodeType.FUNCTION", "builtins/str/NodeType.CLASS"),
    (
        "examples/random_function/NodeType.FUNCTION",
        "examples/random_function/NodeType.FUNCTION",
    ),
]

snapshots["test_get_dependency_edges_match_snapshot[With external nodes-Module] 1"] = [
    ("/examples/NodeType.MODULE", "builtins/bool/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "builtins/int/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "builtins/object/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "builtins/str/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "builtins/type/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "dataclasses/dataclass/NodeType.FUNCTION"),
    ("/examples/NodeType.MODULE", "enum/Enum/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "enum/auto/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "examples/Animal/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "examples/AnimalType/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "examples/BareClass/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "examples/BareClassExtension/NodeType.CLASS"),
    (
        "/examples/NodeType.MODULE",
        "examples/ClassWithHackyDocumentation/NodeType.CLASS",
    ),
    ("/examples/NodeType.MODULE", "examples/Course/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "examples/Person/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "examples/StringTypedClass/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "examples/Student/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "examples/examples.foldermodule/NodeType.MODULE"),
    ("/examples/NodeType.MODULE", "examples/examples.submodule/NodeType.MODULE"),
    ("/examples/NodeType.MODULE", "examples/random_function/NodeType.FUNCTION"),
    ("/examples/NodeType.MODULE", "typing/List/NodeType.CLASS"),
]

snapshots[
    "test_get_dependency_edges_match_snapshot[Without external nodes-Class] 1"
] = [
    ("examples/Animal/NodeType.CLASS", "examples/Animal/NodeType.CLASS"),
    ("examples/Animal/NodeType.CLASS", "examples/AnimalType/NodeType.CLASS"),
]

snapshots[
    "test_get_dependency_edges_match_snapshot[Without external nodes-Function] 1"
] = [
    (
        "examples/random_function/NodeType.FUNCTION",
        "examples/random_function/NodeType.FUNCTION",
    )
]

snapshots[
    "test_get_dependency_edges_match_snapshot[Without external nodes-Module] 1"
] = [
    ("/examples/NodeType.MODULE", "examples/Animal/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "examples/AnimalType/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "examples/BareClass/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "examples/BareClassExtension/NodeType.CLASS"),
    (
        "/examples/NodeType.MODULE",
        "examples/ClassWithHackyDocumentation/NodeType.CLASS",
    ),
    ("/examples/NodeType.MODULE", "examples/Course/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "examples/Person/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "examples/StringTypedClass/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "examples/Student/NodeType.CLASS"),
    ("/examples/NodeType.MODULE", "examples/examples.foldermodule/NodeType.MODULE"),
    ("/examples/NodeType.MODULE", "examples/examples.submodule/NodeType.MODULE"),
    ("/examples/NodeType.MODULE", "examples/random_function/NodeType.FUNCTION"),
]

snapshots["test_get_dependency_nodes_match_snapshot[With external nodes-Class] 1"] = [
    "builtins/str/NodeType.CLASS",
    "dataclasses/dataclass/NodeType.FUNCTION",
    "examples/Animal/NodeType.CLASS",
    "examples/AnimalType/NodeType.CLASS",
    "typing/List/NodeType.CLASS",
]

snapshots[
    "test_get_dependency_nodes_match_snapshot[With external nodes-Function] 1"
] = ["builtins/str/NodeType.CLASS", "examples/random_function/NodeType.FUNCTION"]

snapshots["test_get_dependency_nodes_match_snapshot[With external nodes-Module] 1"] = [
    "builtins/bool/NodeType.CLASS",
    "builtins/int/NodeType.CLASS",
    "builtins/object/NodeType.CLASS",
    "builtins/str/NodeType.CLASS",
    "builtins/type/NodeType.CLASS",
    "dataclasses/dataclass/NodeType.FUNCTION",
    "enum/Enum/NodeType.CLASS",
    "enum/auto/NodeType.CLASS",
    "examples/Animal/NodeType.CLASS",
    "examples/AnimalType/NodeType.CLASS",
    "examples/BareClass/NodeType.CLASS",
    "examples/BareClassExtension/NodeType.CLASS",
    "examples/ClassWithHackyDocumentation/NodeType.CLASS",
    "examples/Course/NodeType.CLASS",
    "examples/Person/NodeType.CLASS",
    "examples/StringTypedClass/NodeType.CLASS",
    "examples/Student/NodeType.CLASS",
    "examples/examples.foldermodule/NodeType.MODULE",
    "examples/examples.submodule/NodeType.MODULE",
    "examples/random_function/NodeType.FUNCTION",
    "typing/List/NodeType.CLASS",
]

snapshots[
    "test_get_dependency_nodes_match_snapshot[Without external nodes-Class] 1"
] = ["examples/Animal/NodeType.CLASS", "examples/AnimalType/NodeType.CLASS"]

snapshots[
    "test_get_dependency_nodes_match_snapshot[Without external nodes-Function] 1"
] = ["examples/random_function/NodeType.FUNCTION"]

snapshots[
    "test_get_dependency_nodes_match_snapshot[Without external nodes-Module] 1"
] = [
    "examples/Animal/NodeType.CLASS",
    "examples/AnimalType/NodeType.CLASS",
    "examples/BareClass/NodeType.CLASS",
    "examples/BareClassExtension/NodeType.CLASS",
    "examples/ClassWithHackyDocumentation/NodeType.CLASS",
    "examples/Course/NodeType.CLASS",
    "examples/Person/NodeType.CLASS",
    "examples/StringTypedClass/NodeType.CLASS",
    "examples/Student/NodeType.CLASS",
    "examples/examples.foldermodule/NodeType.MODULE",
    "examples/examples.submodule/NodeType.MODULE",
    "examples/random_function/NodeType.FUNCTION",
]

snapshots[
    "test_get_dependency_nodes_with_parents_match_snapshot[With external nodes-Class] 1"
] = [
    "/builtins/NodeType.MODULE",
    "/dataclasses/NodeType.MODULE",
    "/examples/NodeType.MODULE",
    "/typing/NodeType.MODULE",
    "builtins/str/NodeType.CLASS",
    "dataclasses/dataclass/NodeType.FUNCTION",
    "examples/Animal/NodeType.CLASS",
    "examples/AnimalType/NodeType.CLASS",
    "typing/List/NodeType.CLASS",
]

snapshots[
    "test_get_dependency_nodes_with_parents_match_snapshot[With external nodes-Function] 1"
] = [
    "/builtins/NodeType.MODULE",
    "/examples/NodeType.MODULE",
    "builtins/str/NodeType.CLASS",
    "examples/random_function/NodeType.FUNCTION",
]

snapshots[
    "test_get_dependency_nodes_with_parents_match_snapshot[With external nodes-Module] 1"
] = [
    "/builtins/NodeType.MODULE",
    "/dataclasses/NodeType.MODULE",
    "/enum/NodeType.MODULE",
    "/examples/NodeType.MODULE",
    "/typing/NodeType.MODULE",
    "builtins/bool/NodeType.CLASS",
    "builtins/int/NodeType.CLASS",
    "builtins/object/NodeType.CLASS",
    "builtins/str/NodeType.CLASS",
    "builtins/type/NodeType.CLASS",
    "dataclasses/dataclass/NodeType.FUNCTION",
    "enum/Enum/NodeType.CLASS",
    "enum/auto/NodeType.CLASS",
    "examples/Animal/NodeType.CLASS",
    "examples/AnimalType/NodeType.CLASS",
    "examples/BareClass/NodeType.CLASS",
    "examples/BareClassExtension/NodeType.CLASS",
    "examples/ClassWithHackyDocumentation/NodeType.CLASS",
    "examples/Course/NodeType.CLASS",
    "examples/Person/NodeType.CLASS",
    "examples/StringTypedClass/NodeType.CLASS",
    "examples/Student/NodeType.CLASS",
    "examples/examples.foldermodule/NodeType.MODULE",
    "examples/examples.submodule/NodeType.MODULE",
    "examples/random_function/NodeType.FUNCTION",
    "typing/List/NodeType.CLASS",
]

snapshots[
    "test_get_dependency_nodes_with_parents_match_snapshot[Without external nodes-Class] 1"
] = [
    "/builtins/NodeType.MODULE",
    "/dataclasses/NodeType.MODULE",
    "/examples/NodeType.MODULE",
    "/typing/NodeType.MODULE",
    "builtins/str/NodeType.CLASS",
    "dataclasses/dataclass/NodeType.FUNCTION",
    "examples/Animal/NodeType.CLASS",
    "examples/AnimalType/NodeType.CLASS",
    "typing/List/NodeType.CLASS",
]

snapshots[
    "test_get_dependency_nodes_with_parents_match_snapshot[Without external nodes-Function] 1"
] = [
    "/builtins/NodeType.MODULE",
    "/examples/NodeType.MODULE",
    "builtins/str/NodeType.CLASS",
    "examples/random_function/NodeType.FUNCTION",
]

snapshots[
    "test_get_dependency_nodes_with_parents_match_snapshot[Without external nodes-Module] 1"
] = [
    "/builtins/NodeType.MODULE",
    "/dataclasses/NodeType.MODULE",
    "/enum/NodeType.MODULE",
    "/examples/NodeType.MODULE",
    "/typing/NodeType.MODULE",
    "builtins/bool/NodeType.CLASS",
    "builtins/int/NodeType.CLASS",
    "builtins/object/NodeType.CLASS",
    "builtins/str/NodeType.CLASS",
    "builtins/type/NodeType.CLASS",
    "dataclasses/dataclass/NodeType.FUNCTION",
    "enum/Enum/NodeType.CLASS",
    "enum/auto/NodeType.CLASS",
    "examples/Animal/NodeType.CLASS",
    "examples/AnimalType/NodeType.CLASS",
    "examples/BareClass/NodeType.CLASS",
    "examples/BareClassExtension/NodeType.CLASS",
    "examples/ClassWithHackyDocumentation/NodeType.CLASS",
    "examples/Course/NodeType.CLASS",
    "examples/Person/NodeType.CLASS",
    "examples/StringTypedClass/NodeType.CLASS",
    "examples/Student/NodeType.CLASS",
    "examples/examples.foldermodule/NodeType.MODULE",
    "examples/examples.submodule/NodeType.MODULE",
    "examples/random_function/NodeType.FUNCTION",
    "typing/List/NodeType.CLASS",
]
