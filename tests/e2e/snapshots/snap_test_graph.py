# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_happy_path_create_graph 1"] = (
    [
        "/builtins/NodeType.MODULE",
        "/dataclasses/NodeType.MODULE",
        "/enum/NodeType.MODULE",
        "/examples/NodeType.MODULE",
        "/typing/NodeType.MODULE",
        "Animal/hates/NodeType.FUNCTION",
        "FooTesterTen/test/NodeType.FUNCTION",
        "StringTypedClass/student/NodeType.FUNCTION",
        "StringTypedClass/to/NodeType.FUNCTION",
        "builtins/bool/NodeType.CLASS",
        "builtins/int/NodeType.CLASS",
        "builtins/object/NodeType.CLASS",
        "builtins/str/NodeType.CLASS",
        "builtins/type/NodeType.CLASS",
        "dataclasses/dataclass/NodeType.FUNCTION",
        "enum/Enum/NodeType.CLASS",
        "enum/auto/NodeType.CLASS",
        "examples.submodule.classes/FooTesterTen/NodeType.CLASS",
        "examples.submodule.classes/foo_ten/NodeType.FUNCTION",
        "examples.submodule/examples.submodule.classes/NodeType.MODULE",
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
    ],
    [
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
        ("Animal/hates/NodeType.FUNCTION", "examples/AnimalType/NodeType.CLASS"),
        (
            "StringTypedClass/student/NodeType.FUNCTION",
            "examples/Course/NodeType.CLASS",
        ),
        (
            "StringTypedClass/student/NodeType.FUNCTION",
            "examples/Student/NodeType.CLASS",
        ),
        (
            "examples.submodule/examples.submodule.classes/NodeType.MODULE",
            "examples.submodule.classes/FooTesterTen/NodeType.CLASS",
        ),
        (
            "examples.submodule/examples.submodule.classes/NodeType.MODULE",
            "examples.submodule.classes/foo_ten/NodeType.FUNCTION",
        ),
        ("examples/Animal/NodeType.CLASS", "examples/AnimalType/NodeType.CLASS"),
        (
            "examples/BareClassExtension/NodeType.CLASS",
            "examples/BareClass/NodeType.CLASS",
        ),
        ("examples/StringTypedClass/NodeType.CLASS", "examples/Course/NodeType.CLASS"),
        ("examples/StringTypedClass/NodeType.CLASS", "examples/Student/NodeType.CLASS"),
        ("examples/Student/NodeType.CLASS", "examples/Course/NodeType.CLASS"),
        ("examples/Student/NodeType.CLASS", "examples/Person/NodeType.CLASS"),
        (
            "examples/examples.submodule/NodeType.MODULE",
            "examples.submodule.classes/FooTesterTen/NodeType.CLASS",
        ),
        (
            "examples/examples.submodule/NodeType.MODULE",
            "examples.submodule.classes/foo_ten/NodeType.FUNCTION",
        ),
        (
            "examples/examples.submodule/NodeType.MODULE",
            "examples.submodule/examples.submodule.classes/NodeType.MODULE",
        ),
    ],
)
