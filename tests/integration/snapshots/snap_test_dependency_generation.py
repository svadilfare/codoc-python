# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_get_dependency_edges_match_snapshot[With external nodes-Class] 1"] = [
    ("Animal/NodeType.CLASS/examples", "Animal/NodeType.CLASS/examples"),
    ("Animal/NodeType.CLASS/examples", "AnimalType/NodeType.CLASS/examples"),
    ("Animal/NodeType.CLASS/examples", "List/NodeType.CLASS/typing"),
    ("Animal/NodeType.CLASS/examples", "dataclass/NodeType.FUNCTION/dataclasses"),
    ("Animal/NodeType.CLASS/examples", "str/NodeType.CLASS/builtins"),
]

snapshots[
    "test_get_dependency_edges_match_snapshot[With external nodes-Function] 1"
] = [
    (
        "random_function/NodeType.FUNCTION/examples",
        "random_function/NodeType.FUNCTION/examples",
    ),
    ("random_function/NodeType.FUNCTION/examples", "str/NodeType.CLASS/builtins"),
]

snapshots["test_get_dependency_edges_match_snapshot[With external nodes-Module] 1"] = [
    ("examples/NodeType.MODULE/", "Animal/NodeType.CLASS/examples"),
    ("examples/NodeType.MODULE/", "AnimalType/NodeType.CLASS/examples"),
    ("examples/NodeType.MODULE/", "BareClass/NodeType.CLASS/examples"),
    ("examples/NodeType.MODULE/", "BareClassExtension/NodeType.CLASS/examples"),
    (
        "examples/NodeType.MODULE/",
        "ClassWithHackyDocumentation/NodeType.CLASS/examples",
    ),
    ("examples/NodeType.MODULE/", "Course/NodeType.CLASS/examples"),
    ("examples/NodeType.MODULE/", "Enum/NodeType.CLASS/enum"),
    ("examples/NodeType.MODULE/", "Exception/NodeType.EXCEPTION/builtins"),
    ("examples/NodeType.MODULE/", "List/NodeType.CLASS/typing"),
    ("examples/NodeType.MODULE/", "Person/NodeType.CLASS/examples"),
    ("examples/NodeType.MODULE/", "RandomError/NodeType.EXCEPTION/examples"),
    ("examples/NodeType.MODULE/", "StringTypedClass/NodeType.CLASS/examples"),
    ("examples/NodeType.MODULE/", "Student/NodeType.CLASS/examples"),
    ("examples/NodeType.MODULE/", "auto/NodeType.CLASS/enum"),
    ("examples/NodeType.MODULE/", "bool/NodeType.CLASS/builtins"),
    ("examples/NodeType.MODULE/", "dataclass/NodeType.FUNCTION/dataclasses"),
    ("examples/NodeType.MODULE/", "examples.foldermodule/NodeType.MODULE/examples"),
    ("examples/NodeType.MODULE/", "examples.submodule/NodeType.MODULE/examples"),
    ("examples/NodeType.MODULE/", "int/NodeType.CLASS/builtins"),
    ("examples/NodeType.MODULE/", "object/NodeType.CLASS/builtins"),
    ("examples/NodeType.MODULE/", "random_function/NodeType.FUNCTION/examples"),
    ("examples/NodeType.MODULE/", "str/NodeType.CLASS/builtins"),
    ("examples/NodeType.MODULE/", "type/NodeType.CLASS/builtins"),
]

snapshots[
    "test_get_dependency_edges_match_snapshot[Without external nodes-Class] 1"
] = [
    ("Animal/NodeType.CLASS/examples", "Animal/NodeType.CLASS/examples"),
    ("Animal/NodeType.CLASS/examples", "AnimalType/NodeType.CLASS/examples"),
]

snapshots[
    "test_get_dependency_edges_match_snapshot[Without external nodes-Function] 1"
] = [
    (
        "random_function/NodeType.FUNCTION/examples",
        "random_function/NodeType.FUNCTION/examples",
    )
]

snapshots[
    "test_get_dependency_edges_match_snapshot[Without external nodes-Module] 1"
] = [
    ("examples/NodeType.MODULE/", "Animal/NodeType.CLASS/examples"),
    ("examples/NodeType.MODULE/", "AnimalType/NodeType.CLASS/examples"),
    ("examples/NodeType.MODULE/", "BareClass/NodeType.CLASS/examples"),
    ("examples/NodeType.MODULE/", "BareClassExtension/NodeType.CLASS/examples"),
    (
        "examples/NodeType.MODULE/",
        "ClassWithHackyDocumentation/NodeType.CLASS/examples",
    ),
    ("examples/NodeType.MODULE/", "Course/NodeType.CLASS/examples"),
    ("examples/NodeType.MODULE/", "Person/NodeType.CLASS/examples"),
    ("examples/NodeType.MODULE/", "RandomError/NodeType.EXCEPTION/examples"),
    ("examples/NodeType.MODULE/", "StringTypedClass/NodeType.CLASS/examples"),
    ("examples/NodeType.MODULE/", "Student/NodeType.CLASS/examples"),
    ("examples/NodeType.MODULE/", "examples.foldermodule/NodeType.MODULE/examples"),
    ("examples/NodeType.MODULE/", "examples.submodule/NodeType.MODULE/examples"),
    ("examples/NodeType.MODULE/", "random_function/NodeType.FUNCTION/examples"),
]

snapshots["test_get_dependency_nodes_match_snapshot[With external nodes-Class] 1"] = [
    "Animal/NodeType.CLASS/examples",
    "AnimalType/NodeType.CLASS/examples",
    "List/NodeType.CLASS/typing",
    "dataclass/NodeType.FUNCTION/dataclasses",
    "str/NodeType.CLASS/builtins",
]

snapshots[
    "test_get_dependency_nodes_match_snapshot[With external nodes-Function] 1"
] = ["random_function/NodeType.FUNCTION/examples", "str/NodeType.CLASS/builtins"]

snapshots["test_get_dependency_nodes_match_snapshot[With external nodes-Module] 1"] = [
    "Animal/NodeType.CLASS/examples",
    "AnimalType/NodeType.CLASS/examples",
    "BareClass/NodeType.CLASS/examples",
    "BareClassExtension/NodeType.CLASS/examples",
    "ClassWithHackyDocumentation/NodeType.CLASS/examples",
    "Course/NodeType.CLASS/examples",
    "Enum/NodeType.CLASS/enum",
    "Exception/NodeType.EXCEPTION/builtins",
    "List/NodeType.CLASS/typing",
    "Person/NodeType.CLASS/examples",
    "RandomError/NodeType.EXCEPTION/examples",
    "StringTypedClass/NodeType.CLASS/examples",
    "Student/NodeType.CLASS/examples",
    "auto/NodeType.CLASS/enum",
    "bool/NodeType.CLASS/builtins",
    "dataclass/NodeType.FUNCTION/dataclasses",
    "examples.foldermodule/NodeType.MODULE/examples",
    "examples.submodule/NodeType.MODULE/examples",
    "int/NodeType.CLASS/builtins",
    "object/NodeType.CLASS/builtins",
    "random_function/NodeType.FUNCTION/examples",
    "str/NodeType.CLASS/builtins",
    "type/NodeType.CLASS/builtins",
]

snapshots[
    "test_get_dependency_nodes_match_snapshot[Without external nodes-Class] 1"
] = ["Animal/NodeType.CLASS/examples", "AnimalType/NodeType.CLASS/examples"]

snapshots[
    "test_get_dependency_nodes_match_snapshot[Without external nodes-Function] 1"
] = ["random_function/NodeType.FUNCTION/examples"]

snapshots[
    "test_get_dependency_nodes_match_snapshot[Without external nodes-Module] 1"
] = [
    "Animal/NodeType.CLASS/examples",
    "AnimalType/NodeType.CLASS/examples",
    "BareClass/NodeType.CLASS/examples",
    "BareClassExtension/NodeType.CLASS/examples",
    "ClassWithHackyDocumentation/NodeType.CLASS/examples",
    "Course/NodeType.CLASS/examples",
    "Person/NodeType.CLASS/examples",
    "RandomError/NodeType.EXCEPTION/examples",
    "StringTypedClass/NodeType.CLASS/examples",
    "Student/NodeType.CLASS/examples",
    "examples.foldermodule/NodeType.MODULE/examples",
    "examples.submodule/NodeType.MODULE/examples",
    "random_function/NodeType.FUNCTION/examples",
]

snapshots[
    "test_get_dependency_nodes_with_parents_match_snapshot[With external nodes-Class] 1"
] = [
    "Animal/NodeType.CLASS/examples",
    "AnimalType/NodeType.CLASS/examples",
    "List/NodeType.CLASS/typing",
    "builtins/NodeType.MODULE/",
    "dataclass/NodeType.FUNCTION/dataclasses",
    "dataclasses/NodeType.MODULE/",
    "examples/NodeType.MODULE/",
    "str/NodeType.CLASS/builtins",
    "typing/NodeType.MODULE/",
]

snapshots[
    "test_get_dependency_nodes_with_parents_match_snapshot[With external nodes-Function] 1"
] = [
    "builtins/NodeType.MODULE/",
    "examples/NodeType.MODULE/",
    "random_function/NodeType.FUNCTION/examples",
    "str/NodeType.CLASS/builtins",
]

snapshots[
    "test_get_dependency_nodes_with_parents_match_snapshot[With external nodes-Module] 1"
] = [
    "Animal/NodeType.CLASS/examples",
    "AnimalType/NodeType.CLASS/examples",
    "BareClass/NodeType.CLASS/examples",
    "BareClassExtension/NodeType.CLASS/examples",
    "ClassWithHackyDocumentation/NodeType.CLASS/examples",
    "Course/NodeType.CLASS/examples",
    "Enum/NodeType.CLASS/enum",
    "Exception/NodeType.EXCEPTION/builtins",
    "List/NodeType.CLASS/typing",
    "Person/NodeType.CLASS/examples",
    "RandomError/NodeType.EXCEPTION/examples",
    "StringTypedClass/NodeType.CLASS/examples",
    "Student/NodeType.CLASS/examples",
    "auto/NodeType.CLASS/enum",
    "bool/NodeType.CLASS/builtins",
    "builtins/NodeType.MODULE/",
    "dataclass/NodeType.FUNCTION/dataclasses",
    "dataclasses/NodeType.MODULE/",
    "enum/NodeType.MODULE/",
    "examples.foldermodule/NodeType.MODULE/examples",
    "examples.submodule/NodeType.MODULE/examples",
    "examples/NodeType.MODULE/",
    "int/NodeType.CLASS/builtins",
    "object/NodeType.CLASS/builtins",
    "random_function/NodeType.FUNCTION/examples",
    "str/NodeType.CLASS/builtins",
    "type/NodeType.CLASS/builtins",
    "typing/NodeType.MODULE/",
]

snapshots[
    "test_get_dependency_nodes_with_parents_match_snapshot[Without external nodes-Class] 1"
] = [
    "Animal/NodeType.CLASS/examples",
    "AnimalType/NodeType.CLASS/examples",
    "List/NodeType.CLASS/typing",
    "builtins/NodeType.MODULE/",
    "dataclass/NodeType.FUNCTION/dataclasses",
    "dataclasses/NodeType.MODULE/",
    "examples/NodeType.MODULE/",
    "str/NodeType.CLASS/builtins",
    "typing/NodeType.MODULE/",
]

snapshots[
    "test_get_dependency_nodes_with_parents_match_snapshot[Without external nodes-Function] 1"
] = [
    "builtins/NodeType.MODULE/",
    "examples/NodeType.MODULE/",
    "random_function/NodeType.FUNCTION/examples",
    "str/NodeType.CLASS/builtins",
]

snapshots[
    "test_get_dependency_nodes_with_parents_match_snapshot[Without external nodes-Module] 1"
] = [
    "Animal/NodeType.CLASS/examples",
    "AnimalType/NodeType.CLASS/examples",
    "BareClass/NodeType.CLASS/examples",
    "BareClassExtension/NodeType.CLASS/examples",
    "ClassWithHackyDocumentation/NodeType.CLASS/examples",
    "Course/NodeType.CLASS/examples",
    "Enum/NodeType.CLASS/enum",
    "Exception/NodeType.EXCEPTION/builtins",
    "List/NodeType.CLASS/typing",
    "Person/NodeType.CLASS/examples",
    "RandomError/NodeType.EXCEPTION/examples",
    "StringTypedClass/NodeType.CLASS/examples",
    "Student/NodeType.CLASS/examples",
    "auto/NodeType.CLASS/enum",
    "bool/NodeType.CLASS/builtins",
    "builtins/NodeType.MODULE/",
    "dataclass/NodeType.FUNCTION/dataclasses",
    "dataclasses/NodeType.MODULE/",
    "enum/NodeType.MODULE/",
    "examples.foldermodule/NodeType.MODULE/examples",
    "examples.submodule/NodeType.MODULE/examples",
    "examples/NodeType.MODULE/",
    "int/NodeType.CLASS/builtins",
    "object/NodeType.CLASS/builtins",
    "random_function/NodeType.FUNCTION/examples",
    "str/NodeType.CLASS/builtins",
    "type/NodeType.CLASS/builtins",
    "typing/NodeType.MODULE/",
]
