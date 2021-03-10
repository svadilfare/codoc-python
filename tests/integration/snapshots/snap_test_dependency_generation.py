# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots["TestGetDependencyEdges.test_class_match_snapshot 1"] = frozenset(
    [
        GenericRepr(
            "Dependency(from_node='examples.AnimalNodeType.CLASS', to_node='dataclasses.dataclassNodeType.FUNCTION')"
        ),
        GenericRepr(
            "Dependency(from_node='examples.AnimalNodeType.CLASS', to_node='examples.AnimalTypeNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='examples.AnimalNodeType.CLASS', to_node='typing.ListNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='examples.AnimalNodeType.CLASS', to_node='builtins.strNodeType.CLASS')"
        ),
    ]
)

snapshots["TestGetDependencyEdges.test_dogfood_match_snapshot 1"] = frozenset(
    [
        GenericRepr(
            "Dependency(from_node='codoc.service.parsing.dependency.get_dependency_edgesNodeType.FUNCTION', to_node='codoc.domain.model.DependencyNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='codoc.service.parsing.dependency.get_dependency_edgesNodeType.FUNCTION', to_node='codoc.service.parsing.dependency.DependencyInspectorNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='codoc.service.parsing.dependency.get_dependency_edgesNodeType.FUNCTION', to_node='codoc.service.parsing.node.create_node_from_objectNodeType.FUNCTION')"
        ),
        GenericRepr(
            "Dependency(from_node='codoc.service.parsing.dependency.get_dependency_edgesNodeType.FUNCTION', to_node='typing.FrozenSetNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='codoc.service.parsing.dependency.get_dependency_edgesNodeType.FUNCTION', to_node='codoc.service.parsing.node.get_parent_of_objectNodeType.FUNCTION')"
        ),
        GenericRepr(
            "Dependency(from_node='codoc.service.parsing.dependency.get_dependency_edgesNodeType.FUNCTION', to_node='typing.NoneNodeType.CLASS')"
        ),
    ]
)

snapshots["TestGetDependencyEdges.test_function_match_snapshot 1"] = frozenset(
    [
        GenericRepr(
            "Dependency(from_node='examples.random_functionNodeType.FUNCTION', to_node='builtins.strNodeType.CLASS')"
        )
    ]
)

snapshots["TestGetDependencyEdges.test_module_match_snapshot 1"] = frozenset(
    [
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='examples.AnimalTypeNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='typing.ListNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='examples.CourseNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='builtins.typeNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='examples.PersonNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='builtins.intNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='builtins.objectNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='examples.StringTypedClassNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='examples.StudentNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='examples.AnimalNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='dataclasses.dataclassNodeType.FUNCTION')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='enum.autoNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='examples.BareClassExtensionNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='examples.ClassWithHackyDocumentationNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='examples.examples.submoduleNodeType.MODULE')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='builtins.strNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='builtins.boolNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='examples.BareClassNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='enum.EnumNodeType.CLASS')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='examples.random_functionNodeType.FUNCTION')"
        ),
        GenericRepr(
            "Dependency(from_node='None.examplesNodeType.MODULE', to_node='examples.examples.foldermoduleNodeType.MODULE')"
        ),
    ]
)

snapshots["TestGetDependencyNodes.test_class_match_snapshot 1"] = GenericRepr(
    "<generator object DependencyInspector.get_dependency_nodes.<locals>.<genexpr> at 0x100000000>"
)

snapshots["TestGetDependencyNodes.test_dogfood_match_snapshot 1"] = GenericRepr(
    "<generator object DependencyInspector.get_dependency_nodes.<locals>.<genexpr> at 0x100000000>"
)

snapshots["TestGetDependencyNodes.test_function_match_snapshot 1"] = GenericRepr(
    "<generator object DependencyInspector.get_dependency_nodes.<locals>.<genexpr> at 0x100000000>"
)

snapshots["TestGetDependencyNodes.test_module_match_snapshot 1"] = GenericRepr(
    "<generator object DependencyInspector.get_dependency_nodes.<locals>.<genexpr> at 0x100000000>"
)

snapshots["TestGetDependencyNodesAndParents.test_class_match_snapshot 1"] = frozenset(
    [
        GenericRepr(
            "Node(identifier='builtins.strNodeType.CLASS', name='str', description=\"str(object='') -> str\\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\\n\\nCreate a new string object from the given object. If encoding or\\nerrors is specified, then the object must expose a data buffer\\nthat will be decoded using the given encoding and error handler.\\nOtherwise, returns the result of object.__str__() (if defined)\\nor repr(object).\\nencoding defaults to sys.getdefaultencoding().\\nerrors defaults to 'strict'.\", of_type=<NodeType.CLASS: 1>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='None.examplesNodeType.MODULE', name='examples', description='', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='dataclasses.dataclassNodeType.FUNCTION', name='dataclass', description='Returns the same class as was passed in, with dunder methods\\nadded based on the fields defined in the class.\\n\\nExamines PEP 526 __annotations__ to determine fields.\\n\\nIf init is true, an __init__() method is added to the class. If\\nrepr is true, a __repr__() method is added. If order is true, rich\\ncomparison dunder methods are added. If unsafe_hash is true, a\\n__hash__() method function is added. If frozen is true, fields may\\nnot be assigned to after instance creation.', of_type=<NodeType.FUNCTION: 2>, parent_identifier='None.dataclassesNodeType.MODULE', path=None, args=('cls',), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples.AnimalTypeNodeType.CLASS', name='AnimalType', description='An enumeration.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.examplesNodeType.MODULE', path=None, args=('cls', 'value', 'names'), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='None.builtinsNodeType.MODULE', name='builtins', description=\"Built-in functions, exceptions, and other objects.\\n\\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.\", of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='None.typingNodeType.MODULE', name='typing', description='The typing module: Support for gradual typing as defined by PEP 484.\\n\\nAt large scale, the structure of the module is following:\\n* Imports and exports, all public names should be explicitly added to __all__.\\n* Internal helper functions: these should never be used in code outside this module.\\n* _SpecialForm and its instances (special forms): Any, NoReturn, ClassVar, Union, Optional\\n* Two classes whose instances can be type arguments in addition to types: ForwardRef and TypeVar\\n* The core of internal generics API: _GenericAlias and _VariadicGenericAlias, the latter is\\n  currently only used by Tuple and Callable. All subscripted types like X[int], Union[int, str],\\n  etc., are instances of either of these classes.\\n* The public counterpart of the generics API consists of two classes: Generic and Protocol.\\n* Public helper functions: get_type_hints, overload, cast, no_type_check,\\n  no_type_check_decorator.\\n* Generic aliases for collections.abc ABCs and few additional protocols.\\n* Special types: NewType, NamedTuple, TypedDict.\\n* Wrapper submodules for re and io related types.', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='None.dataclassesNodeType.MODULE', name='dataclasses', description='', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='typing.ListNodeType.CLASS', name='List', description='A generic version of list.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.typingNodeType.MODULE', path=None, args=('self',), lines=None)"
        ),
    ]
)

snapshots["TestGetDependencyNodesAndParents.test_dogfood_match_snapshot 1"] = frozenset(
    [
        GenericRepr(
            "Node(identifier='codoc.service.parsing.codoc.service.parsing.nodeNodeType.MODULE', name='codoc.service.parsing.node', description='', of_type=<NodeType.MODULE: 3>, parent_identifier='codoc.service.codoc.service.parsingNodeType.MODULE', path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='codoc.codoc.serviceNodeType.MODULE', name='codoc.service', description='', of_type=<NodeType.MODULE: 3>, parent_identifier='None.codocNodeType.MODULE', path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='codoc.domain.codoc.domain.modelNodeType.MODULE', name='codoc.domain.model', description='', of_type=<NodeType.MODULE: 3>, parent_identifier='codoc.codoc.domainNodeType.MODULE', path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='typing.FrozenSetNodeType.CLASS', name='FrozenSet', description='A generic version of frozenset.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.typingNodeType.MODULE', path=None, args=('self',), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='codoc.service.parsing.node.get_parent_of_objectNodeType.FUNCTION', name='get_parent_of_object', description='', of_type=<NodeType.FUNCTION: 2>, parent_identifier='codoc.service.parsing.codoc.service.parsing.nodeNodeType.MODULE', path=None, args=('obj',), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='None.codocNodeType.MODULE', name='codoc', description='', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='codoc.codoc.domainNodeType.MODULE', name='codoc.domain', description='', of_type=<NodeType.MODULE: 3>, parent_identifier='None.codocNodeType.MODULE', path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='typing.NoneNodeType.CLASS', name=None, description='', of_type=<NodeType.CLASS: 1>, parent_identifier='None.typingNodeType.MODULE', path=None, args=('self',), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='codoc.service.parsing.codoc.service.parsing.dependencyNodeType.MODULE', name='codoc.service.parsing.dependency', description='', of_type=<NodeType.MODULE: 3>, parent_identifier='codoc.service.codoc.service.parsingNodeType.MODULE', path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='codoc.domain.model.NodeNodeType.CLASS', name='Node', description='Nodes represents a given source code item,\\ni.e a class, function or module.\\n\\nIt contains all the meta data as well as the code that\\ndefined the node in question.', of_type=<NodeType.CLASS: 1>, parent_identifier='codoc.domain.codoc.domain.modelNodeType.MODULE', path=None, args=('self', 'identifier', 'name', 'description', 'of_type', 'parent_identifier', 'path', 'args', 'lines'), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='codoc.service.parsing.dependency.DependencyInspectorNodeType.CLASS', name='DependencyInspector', description='Extracts dependencies from a given class or function', of_type=<NodeType.CLASS: 1>, parent_identifier='codoc.service.parsing.codoc.service.parsing.dependencyNodeType.MODULE', path=None, args=('self', 'obj', 'node_creator_function', 'get_parent_function'), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='None.typingNodeType.MODULE', name='typing', description='The typing module: Support for gradual typing as defined by PEP 484.\\n\\nAt large scale, the structure of the module is following:\\n* Imports and exports, all public names should be explicitly added to __all__.\\n* Internal helper functions: these should never be used in code outside this module.\\n* _SpecialForm and its instances (special forms): Any, NoReturn, ClassVar, Union, Optional\\n* Two classes whose instances can be type arguments in addition to types: ForwardRef and TypeVar\\n* The core of internal generics API: _GenericAlias and _VariadicGenericAlias, the latter is\\n  currently only used by Tuple and Callable. All subscripted types like X[int], Union[int, str],\\n  etc., are instances of either of these classes.\\n* The public counterpart of the generics API consists of two classes: Generic and Protocol.\\n* Public helper functions: get_type_hints, overload, cast, no_type_check,\\n  no_type_check_decorator.\\n* Generic aliases for collections.abc ABCs and few additional protocols.\\n* Special types: NewType, NamedTuple, TypedDict.\\n* Wrapper submodules for re and io related types.', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='codoc.service.parsing.node.create_node_from_objectNodeType.FUNCTION', name='create_node_from_object', description='', of_type=<NodeType.FUNCTION: 2>, parent_identifier='codoc.service.parsing.codoc.service.parsing.nodeNodeType.MODULE', path=None, args=('obj',), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='codoc.service.codoc.service.parsingNodeType.MODULE', name='codoc.service.parsing', description='', of_type=<NodeType.MODULE: 3>, parent_identifier='codoc.codoc.serviceNodeType.MODULE', path=None, args=None, lines=None)"
        ),
    ]
)

snapshots[
    "TestGetDependencyNodesAndParents.test_function_match_snapshot 1"
] = frozenset(
    [
        GenericRepr(
            "Node(identifier='builtins.strNodeType.CLASS', name='str', description=\"str(object='') -> str\\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\\n\\nCreate a new string object from the given object. If encoding or\\nerrors is specified, then the object must expose a data buffer\\nthat will be decoded using the given encoding and error handler.\\nOtherwise, returns the result of object.__str__() (if defined)\\nor repr(object).\\nencoding defaults to sys.getdefaultencoding().\\nerrors defaults to 'strict'.\", of_type=<NodeType.CLASS: 1>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='None.builtinsNodeType.MODULE', name='builtins', description=\"Built-in functions, exceptions, and other objects.\\n\\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.\", of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
    ]
)

snapshots["TestGetDependencyNodesAndParents.test_module_match_snapshot 1"] = frozenset(
    [
        GenericRepr(
            "Node(identifier='builtins.strNodeType.CLASS', name='str', description=\"str(object='') -> str\\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\\n\\nCreate a new string object from the given object. If encoding or\\nerrors is specified, then the object must expose a data buffer\\nthat will be decoded using the given encoding and error handler.\\nOtherwise, returns the result of object.__str__() (if defined)\\nor repr(object).\\nencoding defaults to sys.getdefaultencoding().\\nerrors defaults to 'strict'.\", of_type=<NodeType.CLASS: 1>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples.BareClassNodeType.CLASS', name='BareClass', description='', of_type=<NodeType.CLASS: 1>, parent_identifier='None.examplesNodeType.MODULE', path=None, args=(), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='enum.EnumNodeType.CLASS', name='Enum', description='Generic enumeration.\\n\\nDerive from this class to define new enumerations.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.enumNodeType.MODULE', path=None, args=('cls', 'value', 'names'), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples.examples.foldermoduleNodeType.MODULE', name='examples.foldermodule', description='', of_type=<NodeType.MODULE: 3>, parent_identifier='None.examplesNodeType.MODULE', path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples.random_functionNodeType.FUNCTION', name='random_function', description='Will output something COMPLETLY random', of_type=<NodeType.FUNCTION: 2>, parent_identifier='None.examplesNodeType.MODULE', path=None, args=(), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='None.dataclassesNodeType.MODULE', name='dataclasses', description='', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples.CourseNodeType.CLASS', name='Course', description='Course contains information about a specific study direction\\nwith name, year as well as whether it is in the spring or fall', of_type=<NodeType.CLASS: 1>, parent_identifier='None.examplesNodeType.MODULE', path=None, args=('self', 'name', 'year', 'spring'), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='typing.ListNodeType.CLASS', name='List', description='A generic version of list.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.typingNodeType.MODULE', path=None, args=('self',), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='builtins.typeNodeType.CLASS', name='type', description=\"type(object_or_name, bases, dict)\\ntype(object) -> the object's type\\ntype(name, bases, dict) -> a new type\", of_type=<NodeType.CLASS: 1>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples.AnimalTypeNodeType.CLASS', name='AnimalType', description='An enumeration.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.examplesNodeType.MODULE', path=None, args=('cls', 'value', 'names'), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='None.enumNodeType.MODULE', name='enum', description='', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples.PersonNodeType.CLASS', name='Person', description='Person is a human that has a name and an age', of_type=<NodeType.CLASS: 1>, parent_identifier='None.examplesNodeType.MODULE', path=None, args=('self', 'name', 'age'), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='builtins.intNodeType.CLASS', name='int', description=\"int([x]) -> integer\\nint(x, base=10) -> integer\\n\\nConvert a number or string to an integer, or return 0 if no arguments\\nare given.  If x is a number, return x.__int__().  For floating point\\nnumbers, this truncates towards zero.\\n\\nIf x is not a number or if base is given, then x must be a string,\\nbytes, or bytearray instance representing an integer literal in the\\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\\nBase 0 means to interpret the base from the string as an integer literal.\\n>>> int('0b100', base=0)\\n4\", of_type=<NodeType.CLASS: 1>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='builtins.objectNodeType.CLASS', name='object', description='The base class of the class hierarchy.\\n\\nWhen called, it accepts no arguments and returns a new featureless\\ninstance that has no instance attributes and cannot be given any.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=(), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples.StudentNodeType.CLASS', name='Student', description='Student(name: str, age: int, course: examples.Course)', of_type=<NodeType.CLASS: 1>, parent_identifier='None.examplesNodeType.MODULE', path=None, args=('self', 'name', 'age', 'course'), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples.StringTypedClassNodeType.CLASS', name='StringTypedClass', description='', of_type=<NodeType.CLASS: 1>, parent_identifier='None.examplesNodeType.MODULE', path=None, args=(), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples.AnimalNodeType.CLASS', name='Animal', description='Animal(kind: examples.AnimalType, name: str)', of_type=<NodeType.CLASS: 1>, parent_identifier='None.examplesNodeType.MODULE', path=None, args=('self', 'kind', 'name'), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='dataclasses.dataclassNodeType.FUNCTION', name='dataclass', description='Returns the same class as was passed in, with dunder methods\\nadded based on the fields defined in the class.\\n\\nExamines PEP 526 __annotations__ to determine fields.\\n\\nIf init is true, an __init__() method is added to the class. If\\nrepr is true, a __repr__() method is added. If order is true, rich\\ncomparison dunder methods are added. If unsafe_hash is true, a\\n__hash__() method function is added. If frozen is true, fields may\\nnot be assigned to after instance creation.', of_type=<NodeType.FUNCTION: 2>, parent_identifier='None.dataclassesNodeType.MODULE', path=None, args=('cls',), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='None.builtinsNodeType.MODULE', name='builtins', description=\"Built-in functions, exceptions, and other objects.\\n\\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.\", of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='None.typingNodeType.MODULE', name='typing', description='The typing module: Support for gradual typing as defined by PEP 484.\\n\\nAt large scale, the structure of the module is following:\\n* Imports and exports, all public names should be explicitly added to __all__.\\n* Internal helper functions: these should never be used in code outside this module.\\n* _SpecialForm and its instances (special forms): Any, NoReturn, ClassVar, Union, Optional\\n* Two classes whose instances can be type arguments in addition to types: ForwardRef and TypeVar\\n* The core of internal generics API: _GenericAlias and _VariadicGenericAlias, the latter is\\n  currently only used by Tuple and Callable. All subscripted types like X[int], Union[int, str],\\n  etc., are instances of either of these classes.\\n* The public counterpart of the generics API consists of two classes: Generic and Protocol.\\n* Public helper functions: get_type_hints, overload, cast, no_type_check,\\n  no_type_check_decorator.\\n* Generic aliases for collections.abc ABCs and few additional protocols.\\n* Special types: NewType, NamedTuple, TypedDict.\\n* Wrapper submodules for re and io related types.', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='enum.autoNodeType.CLASS', name='auto', description='Instances are replaced with an appropriate value in Enum class suites.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.enumNodeType.MODULE', path=None, args=(), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='None.examplesNodeType.MODULE', name='examples', description='', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples.BareClassExtensionNodeType.CLASS', name='BareClassExtension', description='', of_type=<NodeType.CLASS: 1>, parent_identifier='None.examplesNodeType.MODULE', path=None, args=(), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples.ClassWithHackyDocumentationNodeType.CLASS', name='ClassWithHackyDocumentation', description='DescriptionDescriptionDescriptionDescriptionDescription', of_type=<NodeType.CLASS: 1>, parent_identifier='None.examplesNodeType.MODULE', path=None, args=(), lines=None)"
        ),
        GenericRepr(
            "Node(identifier='examples.examples.submoduleNodeType.MODULE', name='examples.submodule', description='', of_type=<NodeType.MODULE: 3>, parent_identifier='None.examplesNodeType.MODULE', path=None, args=None, lines=None)"
        ),
        GenericRepr(
            "Node(identifier='builtins.boolNodeType.CLASS', name='bool', description='bool(x) -> bool\\n\\nReturns True when the argument x is true, False otherwise.\\nThe builtins True and False are the only two instances of the class bool.\\nThe class bool is a subclass of the class int, and cannot be subclassed.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=None, lines=None)"
        ),
    ]
)
