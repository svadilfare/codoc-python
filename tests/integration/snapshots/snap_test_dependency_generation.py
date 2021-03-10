# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots["test_get_dependency_edges_match_snapshot[Class] 1"] = frozenset(
    [
        GenericRepr(
            "Dependency(from_node='examples/Animal/NodeType.CLASS', to_node='dataclasses/dataclass/NodeType.FUNCTION')"
        ),
        GenericRepr(
            "Dependency(from_node='examples/Animal/NodeType.CLASS', to_node='examples/AnimalType/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='examples/Animal/NodeType.CLASS', to_node='examples/Animal/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='examples/Animal/NodeType.CLASS', to_node='typing/List/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='examples/Animal/NodeType.CLASS', to_node='builtins/str/NodeType.CLASS')"
        ),
    ]
)

snapshots["test_get_dependency_edges_match_snapshot[Function] 1"] = frozenset(
    [
        GenericRepr(
            "Dependency(from_node='examples/random_function/NodeType.FUNCTION', to_node='examples/random_function/NodeType.FUNCTION')"
        ),
        GenericRepr(
            "Dependency(from_node='examples/random_function/NodeType.FUNCTION', to_node='builtins/str/NodeType.CLASS')"
        ),
    ]
)

snapshots["test_get_dependency_edges_match_snapshot[Module] 1"] = frozenset(
    [
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/ClassWithHackyDocumentation/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='typing/List/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='builtins/type/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/examples.foldermodule/NodeType.MODULE')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='builtins/str/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/examples.submodule/NodeType.MODULE')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='dataclasses/dataclass/NodeType.FUNCTION')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/Person/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='builtins/object/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='enum/auto/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/Animal/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/StringTypedClass/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/Course/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='builtins/int/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/BareClass/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/Student/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/BareClassExtension/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/AnimalType/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/random_function/NodeType.FUNCTION')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='enum/Enum/NodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='/examples/NodeType.MODULE', to_node='builtins/bool/NodeType.CLASS')"
        ),
    ]
)

snapshots["test_get_dependency_nodes_match_snapshot[Class] 1"] = GenericRepr(
    "<generator object DependencyInspector.get_dependency_nodes.<locals>.<genexpr> at 0x100000000>"
)

snapshots["test_get_dependency_nodes_match_snapshot[Function] 1"] = GenericRepr(
    "<generator object DependencyInspector.get_dependency_nodes.<locals>.<genexpr> at 0x100000000>"
)

snapshots["test_get_dependency_nodes_match_snapshot[Module] 1"] = GenericRepr(
    "<generator object DependencyInspector.get_dependency_nodes.<locals>.<genexpr> at 0x100000000>"
)

snapshots["test_get_dependency_nodes_with_parents_match_snapshot[Class] 1"] = frozenset(
    [
        GenericRepr(
            "Node(identifier='examples/AnimalType/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples/Animal/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='/dataclasses/NodeType.MODULE', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='typing/List/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='builtins/str/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='/builtins/NodeType.MODULE', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='/examples/NodeType.MODULE', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='/typing/NodeType.MODULE', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='dataclasses/dataclass/NodeType.FUNCTION', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
    ]
)

snapshots[
    "test_get_dependency_nodes_with_parents_match_snapshot[Function] 1"
] = frozenset(
    [
        GenericRepr(
            "Node(identifier='builtins/str/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='/examples/NodeType.MODULE', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='/builtins/NodeType.MODULE', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples/random_function/NodeType.FUNCTION', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
    ]
)

snapshots[
    "test_get_dependency_nodes_with_parents_match_snapshot[Module] 1"
] = frozenset(
    [
        GenericRepr(
            "Node(identifier='examples/ClassWithHackyDocumentation/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='builtins/type/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='typing/List/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='builtins/str/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples/examples.foldermodule/NodeType.MODULE', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples/examples.submodule/NodeType.MODULE', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='dataclasses/dataclass/NodeType.FUNCTION', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='/dataclasses/NodeType.MODULE', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples/Person/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='builtins/object/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='enum/auto/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples/Animal/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples/Course/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples/StringTypedClass/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples/Student/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='builtins/int/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples/BareClass/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples/BareClassExtension/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='/typing/NodeType.MODULE', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples/AnimalType/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='/enum/NodeType.MODULE', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples/random_function/NodeType.FUNCTION', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='enum/Enum/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='/builtins/NodeType.MODULE', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='builtins/bool/NodeType.CLASS', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='/examples/NodeType.MODULE', name='test', description='test', of_type=<NodeType.CLASS: 1>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
    ]
)
