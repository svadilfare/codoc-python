# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_happy_path_create_graph 1"] = (
    [
        "Animal/NodeType.CLASS/examples",
        "AnimalType/NodeType.CLASS/examples",
        "BareClass/NodeType.CLASS/examples",
        "BareClassExtension/NodeType.CLASS/examples",
        "ClassWithHackyDocumentation/NodeType.CLASS/examples",
        "Course/NodeType.CLASS/examples",
        "Enum/NodeType.CLASS/enum",
        "FooTesterTen/NodeType.CLASS/examples.submodule.classes",
        "List/NodeType.CLASS/typing",
        "Person/NodeType.CLASS/examples",
        "StringTypedClass/NodeType.CLASS/examples",
        "Student/NodeType.CLASS/examples",
        "auto/NodeType.CLASS/enum",
        "bool/NodeType.CLASS/builtins",
        "builtins/NodeType.MODULE/",
        "dataclass/NodeType.FUNCTION/dataclasses",
        "dataclasses/NodeType.MODULE/",
        "enum/NodeType.MODULE/",
        "examples.foldermodule/NodeType.MODULE/examples",
        "examples.submodule.classes/NodeType.MODULE/examples.submodule",
        "examples.submodule/NodeType.MODULE/examples",
        "examples/NodeType.MODULE/",
        "foo_ten/NodeType.FUNCTION/examples.submodule.classes",
        "hates/NodeType.FUNCTION/Animal",
        "int/NodeType.CLASS/builtins",
        "object/NodeType.CLASS/builtins",
        "random_function/NodeType.FUNCTION/examples",
        "str/NodeType.CLASS/builtins",
        "student/NodeType.FUNCTION/StringTypedClass",
        "test/NodeType.FUNCTION/FooTesterTen",
        "to/NodeType.FUNCTION/StringTypedClass",
        "type/NodeType.CLASS/builtins",
        "typing/NodeType.MODULE/",
    ],
    [
        ("Animal/NodeType.CLASS/examples", "AnimalType/NodeType.CLASS/examples"),
        (
            "BareClassExtension/NodeType.CLASS/examples",
            "BareClass/NodeType.CLASS/examples",
        ),
        ("StringTypedClass/NodeType.CLASS/examples", "Course/NodeType.CLASS/examples"),
        ("StringTypedClass/NodeType.CLASS/examples", "Student/NodeType.CLASS/examples"),
        ("Student/NodeType.CLASS/examples", "Course/NodeType.CLASS/examples"),
        ("Student/NodeType.CLASS/examples", "Person/NodeType.CLASS/examples"),
        (
            "examples.submodule.classes/NodeType.MODULE/examples.submodule",
            "FooTesterTen/NodeType.CLASS/examples.submodule.classes",
        ),
        (
            "examples.submodule.classes/NodeType.MODULE/examples.submodule",
            "foo_ten/NodeType.FUNCTION/examples.submodule.classes",
        ),
        (
            "examples.submodule/NodeType.MODULE/examples",
            "FooTesterTen/NodeType.CLASS/examples.submodule.classes",
        ),
        (
            "examples.submodule/NodeType.MODULE/examples",
            "examples.submodule.classes/NodeType.MODULE/examples.submodule",
        ),
        (
            "examples.submodule/NodeType.MODULE/examples",
            "foo_ten/NodeType.FUNCTION/examples.submodule.classes",
        ),
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
        ("examples/NodeType.MODULE/", "StringTypedClass/NodeType.CLASS/examples"),
        ("examples/NodeType.MODULE/", "Student/NodeType.CLASS/examples"),
        ("examples/NodeType.MODULE/", "examples.foldermodule/NodeType.MODULE/examples"),
        ("examples/NodeType.MODULE/", "examples.submodule/NodeType.MODULE/examples"),
        ("examples/NodeType.MODULE/", "random_function/NodeType.FUNCTION/examples"),
        ("hates/NodeType.FUNCTION/Animal", "AnimalType/NodeType.CLASS/examples"),
        (
            "student/NodeType.FUNCTION/StringTypedClass",
            "Course/NodeType.CLASS/examples",
        ),
        (
            "student/NodeType.FUNCTION/StringTypedClass",
            "Student/NodeType.CLASS/examples",
        ),
    ],
)
