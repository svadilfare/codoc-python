# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots["test_happy_path_dogfood_creates_graph 1"] = (
    set(
        [
            GenericRepr(
                "Node(identifier='builtins.strNodeType.CLASS', name='str', description=\"str(object='') -> str\\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\\n\\nCreate a new string object from the given object. If encoding or\\nerrors is specified, then the object must expose a data buffer\\nthat will be decoded using the given encoding and error handler.\\nOtherwise, returns the result of object.__str__() (if defined)\\nor repr(object).\\nencoding defaults to sys.getdefaultencoding().\\nerrors defaults to 'strict'.\", of_type=<NodeType.CLASS: 1>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='codoc.domain.codoc.domain.modelNodeType.MODULE', name='codoc.domain.model', description='', of_type=<NodeType.MODULE: 3>, parent_identifier='codoc.codoc.domainNodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='codoc.domain.helpers.ParentNotFoundExceptionNodeType.CLASS', name='ParentNotFoundException', description='Common base class for all non-exit exceptions.', of_type=<NodeType.CLASS: 1>, parent_identifier='codoc.domain.codoc.domain.helpersNodeType.MODULE', path=None, args=('self', 'current_node', 'graph'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='enum.EnumNodeType.CLASS', name='Enum', description='Generic enumeration.\\n\\nDerive from this class to define new enumerations.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.enumNodeType.MODULE', path=None, args=('cls', 'value', 'names'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='typing.SetNodeType.CLASS', name='Set', description='A generic version of set.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.typingNodeType.MODULE', path=None, args=('self',), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='None.dataclassesNodeType.MODULE', name='dataclasses', description='', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='builtins.superNodeType.CLASS', name='super', description='super() -> same as super(__class__, <first argument>)\\nsuper(type) -> unbound super object\\nsuper(type, obj) -> bound super object; requires isinstance(obj, type)\\nsuper(type, type2) -> bound super object; requires issubclass(type2, type)\\nTypical use to call a cooperative superclass method:\\nclass C(B):\\n    def meth(self, arg):\\n        super().meth(arg)\\nThis works for class methods too:\\nclass C(B):\\n    @classmethod\\n    def cmeth(cls, arg):\\n        super().cmeth(arg)', of_type=<NodeType.CLASS: 1>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='builtins.StopIterationNodeType.CLASS', name='StopIteration', description='Signal the end from iterator.__next__().', of_type=<NodeType.CLASS: 1>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='typing.TupleNodeType.CLASS', name='Tuple', description='Tuple type; Tuple[X, Y] is the cross-product type of X and Y.\\n\\nExample: Tuple[T1, T2] is a tuple of two elements corresponding\\nto type variables T1 and T2.  Tuple[int, float, str] is a tuple\\nof an int, a float and a string.\\n\\nTo specify a variable-length tuple of homogeneous type, use Tuple[T, ...].', of_type=<NodeType.CLASS: 1>, parent_identifier='None.typingNodeType.MODULE', path=None, args=('self',), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='builtins.ExceptionNodeType.CLASS', name='Exception', description='Common base class for all non-exit exceptions.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='None.enumNodeType.MODULE', name='enum', description='', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='None.codocNodeType.MODULE', name='codoc', description='', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='builtins.hashNodeType.FUNCTION', name='hash', description='Return the hash value for the given object.\\n\\nTwo objects that compare equal must also have the same hash value, but the\\nreverse is not necessarily true.', of_type=<NodeType.FUNCTION: 2>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=('obj',), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='codoc.domain.model.GraphNodeType.CLASS', name='Graph', description='A Graph is the base element of the system.\\nIt contains both edges (Dependencies) as well as nodes (classes, functions, etc).\\n\\nIt supports a variety of operators.', of_type=<NodeType.CLASS: 1>, parent_identifier='codoc.domain.codoc.domain.modelNodeType.MODULE', path=None, args=('self', 'edges', 'nodes'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='builtins.nextNodeType.FUNCTION', name='next', description='next(iterator[, default])\\n\\nReturn the next item from the iterator. If default is given and the iterator\\nis exhausted, it is returned instead of raising StopIteration.', of_type=<NodeType.FUNCTION: 2>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='builtins.intNodeType.CLASS', name='int', description=\"int([x]) -> integer\\nint(x, base=10) -> integer\\n\\nConvert a number or string to an integer, or return 0 if no arguments\\nare given.  If x is a number, return x.__int__().  For floating point\\nnumbers, this truncates towards zero.\\n\\nIf x is not a number or if base is given, then x must be a string,\\nbytes, or bytearray instance representing an integer literal in the\\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\\nBase 0 means to interpret the base from the string as an integer literal.\\n>>> int('0b100', base=0)\\n4\", of_type=<NodeType.CLASS: 1>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='codoc.domain.model.NodeNodeType.CLASS', name='Node', description='Nodes represents a given source code item,\\ni.e a class, function or module.\\n\\nIt contains all the meta data as well as the code that\\ndefined the node in question.', of_type=<NodeType.CLASS: 1>, parent_identifier='codoc.domain.codoc.domain.modelNodeType.MODULE', path=None, args=('self', 'identifier', 'name', 'description', 'of_type', 'parent_identifier', 'path', 'args', 'lines'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='typing.AnyNodeType.CLASS', name='Any', description='Special type indicating an unconstrained type.\\n\\n- Any is compatible with every type.\\n- Any assumed to have all methods.\\n- All values assumed to be instances of Any.\\n\\nNote that all the above statements are true from the point of view of\\nstatic type checkers. At runtime, Any should not be used with instance\\nor class checks.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.typingNodeType.MODULE', path=None, args=('self',), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='codoc.domain.model.DependencyNodeType.CLASS', name='Dependency', description=\"A Dependency shows that one node depends on another.\\nCurrently it doesn't specify the type of dependency.\", of_type=<NodeType.CLASS: 1>, parent_identifier='codoc.domain.codoc.domain.modelNodeType.MODULE', path=None, args=('self', 'from_node', 'to_node'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='builtins.setNodeType.CLASS', name='set', description='set() -> new empty set object\\nset(iterable) -> new set object\\n\\nBuild an unordered collection of unique elements.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='builtins.objectNodeType.CLASS', name='object', description='The base class of the class hierarchy.\\n\\nWhen called, it accepts no arguments and returns a new featureless\\ninstance that has no instance attributes and cannot be given any.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=(), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='codoc.domain.helpers.get_childrenNodeType.FUNCTION', name='get_children', description='', of_type=<NodeType.FUNCTION: 2>, parent_identifier='codoc.domain.codoc.domain.helpersNodeType.MODULE', path=None, args=('identifier', 'graph'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='codoc.codoc.domainNodeType.MODULE', name='codoc.domain', description='', of_type=<NodeType.MODULE: 3>, parent_identifier='None.codocNodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='codoc.domain.helpers.has_childrenNodeType.FUNCTION', name='has_children', description='', of_type=<NodeType.FUNCTION: 2>, parent_identifier='codoc.domain.codoc.domain.helpersNodeType.MODULE', path=None, args=('identifier', 'graph'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='dataclasses.dataclassNodeType.FUNCTION', name='dataclass', description='Returns the same class as was passed in, with dunder methods\\nadded based on the fields defined in the class.\\n\\nExamines PEP 526 __annotations__ to determine fields.\\n\\nIf init is true, an __init__() method is added to the class. If\\nrepr is true, a __repr__() method is added. If order is true, rich\\ncomparison dunder methods are added. If unsafe_hash is true, a\\n__hash__() method function is added. If frozen is true, fields may\\nnot be assigned to after instance creation.', of_type=<NodeType.FUNCTION: 2>, parent_identifier='None.dataclassesNodeType.MODULE', path=None, args=('cls',), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='codoc.domain.helpers.get_nodeNodeType.FUNCTION', name='get_node', description='', of_type=<NodeType.FUNCTION: 2>, parent_identifier='codoc.domain.codoc.domain.helpersNodeType.MODULE', path=None, args=('identifier', 'graph'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='None.builtinsNodeType.MODULE', name='builtins', description=\"Built-in functions, exceptions, and other objects.\\n\\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.\", of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='None.typingNodeType.MODULE', name='typing', description='The typing module: Support for gradual typing as defined by PEP 484.\\n\\nAt large scale, the structure of the module is following:\\n* Imports and exports, all public names should be explicitly added to __all__.\\n* Internal helper functions: these should never be used in code outside this module.\\n* _SpecialForm and its instances (special forms): Any, NoReturn, ClassVar, Union, Optional\\n* Two classes whose instances can be type arguments in addition to types: ForwardRef and TypeVar\\n* The core of internal generics API: _GenericAlias and _VariadicGenericAlias, the latter is\\n  currently only used by Tuple and Callable. All subscripted types like X[int], Union[int, str],\\n  etc., are instances of either of these classes.\\n* The public counterpart of the generics API consists of two classes: Generic and Protocol.\\n* Public helper functions: get_type_hints, overload, cast, no_type_check,\\n  no_type_check_decorator.\\n* Generic aliases for collections.abc ABCs and few additional protocols.\\n* Special types: NewType, NamedTuple, TypedDict.\\n* Wrapper submodules for re and io related types.', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='codoc.domain.model.identifier_is_in_nodesNodeType.FUNCTION', name='identifier_is_in_nodes', description='', of_type=<NodeType.FUNCTION: 2>, parent_identifier='codoc.domain.codoc.domain.modelNodeType.MODULE', path=None, args=('identifier', 'nodes'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='enum.autoNodeType.CLASS', name='auto', description='Instances are replaced with an appropriate value in Enum class suites.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.enumNodeType.MODULE', path=None, args=(), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='typing.OptionalNodeType.CLASS', name='Optional', description='Optional type.\\n\\nOptional[X] is equivalent to Union[X, None].', of_type=<NodeType.CLASS: 1>, parent_identifier='None.typingNodeType.MODULE', path=None, args=('self',), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='codoc.domain.codoc.domain.helpersNodeType.MODULE', name='codoc.domain.helpers', description='', of_type=<NodeType.MODULE: 3>, parent_identifier='codoc.codoc.domainNodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='builtins.anyNodeType.FUNCTION', name='any', description='Return True if bool(x) is True for any x in the iterable.\\n\\nIf the iterable is empty, return False.', of_type=<NodeType.FUNCTION: 2>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=('iterable',), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='codoc.domain.helpers.NodeIdentifierNotFoundExceptionNodeType.CLASS', name='NodeIdentifierNotFoundException', description='Common base class for all non-exit exceptions.', of_type=<NodeType.CLASS: 1>, parent_identifier='codoc.domain.codoc.domain.helpersNodeType.MODULE', path=None, args=('self', 'identifier', 'graph'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='codoc.domain.helpers.get_parent_nodeNodeType.FUNCTION', name='get_parent_node', description='', of_type=<NodeType.FUNCTION: 2>, parent_identifier='codoc.domain.codoc.domain.helpersNodeType.MODULE', path=None, args=('current_node', 'graph'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='codoc.domain.model.NodeTypeNodeType.CLASS', name='NodeType', description='An enumeration.', of_type=<NodeType.CLASS: 1>, parent_identifier='codoc.domain.codoc.domain.modelNodeType.MODULE', path=None, args=('cls', 'value', 'names'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='builtins.isinstanceNodeType.FUNCTION', name='isinstance', description='Return whether an object is an instance of a class or of a subclass thereof.\\n\\nA tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to\\ncheck against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)\\nor ...`` etc.', of_type=<NodeType.FUNCTION: 2>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=('obj', 'class_or_tuple'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='codoc.domain.model.edge_is_in_nodesNodeType.FUNCTION', name='edge_is_in_nodes', description='', of_type=<NodeType.FUNCTION: 2>, parent_identifier='codoc.domain.codoc.domain.modelNodeType.MODULE', path=None, args=('edge', 'nodes'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='builtins.boolNodeType.CLASS', name='bool', description='bool(x) -> bool\\n\\nReturns True when the argument x is true, False otherwise.\\nThe builtins True and False are the only two instances of the class bool.\\nThe class bool is a subclass of the class int, and cannot be subclassed.', of_type=<NodeType.CLASS: 1>, parent_identifier='None.builtinsNodeType.MODULE', path=None, args=None, lines=None)"
            ),
        ]
    ),
    set(
        [
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.NodeNodeType.CLASS', to_node='typing.OptionalNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='builtins.nextNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='codoc.domain.helpers.get_childrenNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='codoc.domain.helpers.get_nodeNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_nodeNodeType.FUNCTION', to_node='codoc.domain.helpers.NodeIdentifierNotFoundExceptionNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.NodeNodeType.CLASS', to_node='builtins.strNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_parent_nodeNodeType.FUNCTION', to_node='codoc.domain.helpers.get_nodeNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='builtins.anyNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.has_childrenNodeType.FUNCTION', to_node='builtins.strNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.identifier_is_in_nodesNodeType.FUNCTION', to_node='builtins.strNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_childrenNodeType.FUNCTION', to_node='typing.SetNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='typing.OptionalNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.GraphNodeType.CLASS', to_node='codoc.domain.model.DependencyNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.NodeNodeType.CLASS', to_node='builtins.intNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_childrenNodeType.FUNCTION', to_node='codoc.domain.model.GraphNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.NodeTypeNodeType.CLASS', to_node='enum.EnumNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.NodeNodeType.CLASS', to_node='builtins.objectNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_childrenNodeType.FUNCTION', to_node='codoc.domain.model.NodeNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.GraphNodeType.CLASS', to_node='dataclasses.dataclassNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='builtins.StopIterationNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.NodeNodeType.CLASS', to_node='dataclasses.dataclassNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_nodeNodeType.FUNCTION', to_node='codoc.domain.model.GraphNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_childrenNodeType.FUNCTION', to_node='builtins.setNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='builtins.ExceptionNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_nodeNodeType.FUNCTION', to_node='codoc.domain.model.NodeNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.NodeIdentifierNotFoundExceptionNodeType.CLASS', to_node='builtins.ExceptionNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='builtins.strNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.NodeNodeType.CLASS', to_node='codoc.domain.model.NodeTypeNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.has_childrenNodeType.FUNCTION', to_node='builtins.anyNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.ParentNotFoundExceptionNodeType.CLASS', to_node='builtins.ExceptionNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.edge_is_in_nodesNodeType.FUNCTION', to_node='codoc.domain.model.DependencyNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='builtins.intNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.identifier_is_in_nodesNodeType.FUNCTION', to_node='builtins.anyNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='codoc.domain.model.DependencyNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='codoc.domain.helpers.NodeIdentifierNotFoundExceptionNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='codoc.domain.helpers.get_parent_nodeNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='builtins.objectNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_parent_nodeNodeType.FUNCTION', to_node='codoc.domain.helpers.NodeIdentifierNotFoundExceptionNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='dataclasses.dataclassNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.NodeNodeType.CLASS', to_node='typing.TupleNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='enum.autoNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.NodeNodeType.CLASS', to_node='builtins.hashNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.GraphNodeType.CLASS', to_node='typing.AnyNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='builtins.boolNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='builtins.anyNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='codoc.domain.helpers.ParentNotFoundExceptionNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='codoc.domain.model.NodeTypeNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_parent_nodeNodeType.FUNCTION', to_node='codoc.domain.helpers.ParentNotFoundExceptionNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='typing.SetNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='codoc.domain.model.GraphNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.NodeIdentifierNotFoundExceptionNodeType.CLASS', to_node='codoc.domain.model.GraphNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='codoc.domain.model.NodeNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_parent_nodeNodeType.FUNCTION', to_node='codoc.domain.model.GraphNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_parent_nodeNodeType.FUNCTION', to_node='codoc.domain.model.NodeNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='builtins.setNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='typing.TupleNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='codoc.domain.helpers.has_childrenNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='builtins.hashNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.NodeNodeType.CLASS', to_node='builtins.boolNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.ParentNotFoundExceptionNodeType.CLASS', to_node='codoc.domain.model.GraphNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.DependencyNodeType.CLASS', to_node='builtins.strNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='typing.AnyNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.ParentNotFoundExceptionNodeType.CLASS', to_node='codoc.domain.model.NodeNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.GraphNodeType.CLASS', to_node='typing.SetNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_childrenNodeType.FUNCTION', to_node='builtins.strNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.has_childrenNodeType.FUNCTION', to_node='builtins.boolNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_nodeNodeType.FUNCTION', to_node='builtins.strNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.identifier_is_in_nodesNodeType.FUNCTION', to_node='builtins.boolNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.GraphNodeType.CLASS', to_node='codoc.domain.model.NodeNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.DependencyNodeType.CLASS', to_node='builtins.intNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.identifier_is_in_nodesNodeType.FUNCTION', to_node='typing.SetNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.has_childrenNodeType.FUNCTION', to_node='codoc.domain.model.GraphNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='builtins.superNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.NodeIdentifierNotFoundExceptionNodeType.CLASS', to_node='builtins.superNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.edge_is_in_nodesNodeType.FUNCTION', to_node='builtins.boolNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.DependencyNodeType.CLASS', to_node='dataclasses.dataclassNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_nodeNodeType.FUNCTION', to_node='builtins.nextNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.identifier_is_in_nodesNodeType.FUNCTION', to_node='codoc.domain.model.NodeNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='builtins.boolNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='enum.EnumNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.edge_is_in_nodesNodeType.FUNCTION', to_node='typing.SetNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='typing.SetNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.GraphNodeType.CLASS', to_node='builtins.isinstanceNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.NodeNodeType.CLASS', to_node='builtins.isinstanceNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.ParentNotFoundExceptionNodeType.CLASS', to_node='builtins.superNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.GraphNodeType.CLASS', to_node='codoc.domain.model.edge_is_in_nodesNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.edge_is_in_nodesNodeType.FUNCTION', to_node='codoc.domain.model.NodeNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='codoc.domain.model.GraphNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='codoc.domain.model.NodeNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='typing.OptionalNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_parent_nodeNodeType.FUNCTION', to_node='typing.OptionalNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.NodeTypeNodeType.CLASS', to_node='enum.autoNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.edge_is_in_nodesNodeType.FUNCTION', to_node='codoc.domain.model.identifier_is_in_nodesNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='codoc.domain.model.identifier_is_in_nodesNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.model.DependencyNodeType.CLASS', to_node='builtins.hashNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.helpersNodeType.MODULE', to_node='builtins.strNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.NodeIdentifierNotFoundExceptionNodeType.CLASS', to_node='builtins.strNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.helpers.get_nodeNodeType.FUNCTION', to_node='builtins.StopIterationNodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='builtins.isinstanceNodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='codoc.domain.codoc.domain.modelNodeType.MODULE', to_node='codoc.domain.model.edge_is_in_nodesNodeType.FUNCTION')"
            ),
        ]
    ),
)