# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots["test_happy_path_create_graph 1"] = (
    set(
        [
            GenericRepr(
                "Node(identifier='builtins/type/NodeType.CLASS', name='type', description=\"type(object_or_name, bases, dict)\\ntype(object) -> the object's type\\ntype(name, bases, dict) -> a new type\", of_type=<NodeType.CLASS: 1>, parent_identifier='/builtins/NodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='/builtins/NodeType.MODULE', name='builtins', description=\"Built-in functions, exceptions, and other objects.\\n\\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.\", of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='typing/List/NodeType.CLASS', name='List', description='A generic version of list.', of_type=<NodeType.CLASS: 1>, parent_identifier='/typing/NodeType.MODULE', path=None, args=('self',), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='/typing/NodeType.MODULE', name='typing', description='The typing module: Support for gradual typing as defined by PEP 484.\\n\\nAt large scale, the structure of the module is following:\\n* Imports and exports, all public names should be explicitly added to __all__.\\n* Internal helper functions: these should never be used in code outside this module.\\n* _SpecialForm and its instances (special forms): Any, NoReturn, ClassVar, Union, Optional\\n* Two classes whose instances can be type arguments in addition to types: ForwardRef and TypeVar\\n* The core of internal generics API: _GenericAlias and _VariadicGenericAlias, the latter is\\n  currently only used by Tuple and Callable. All subscripted types like X[int], Union[int, str],\\n  etc., are instances of either of these classes.\\n* The public counterpart of the generics API consists of two classes: Generic and Protocol.\\n* Public helper functions: get_type_hints, overload, cast, no_type_check,\\n  no_type_check_decorator.\\n* Generic aliases for collections.abc ABCs and few additional protocols.\\n* Special types: NewType, NamedTuple, TypedDict.\\n* Wrapper submodules for re and io related types.', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='examples/Student/NodeType.CLASS', name='Student', description='Student(name: str, age: int, course: examples.Course)', of_type=<NodeType.CLASS: 1>, parent_identifier='/examples/NodeType.MODULE', path=None, args=('self', 'name', 'age', 'course'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='examples/AnimalType/NodeType.CLASS', name='AnimalType', description='An enumeration.', of_type=<NodeType.CLASS: 1>, parent_identifier='/examples/NodeType.MODULE', path=None, args=('cls', 'value', 'names'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='/enum/NodeType.MODULE', name='enum', description='', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='StringTypedClass/student/NodeType.FUNCTION', name='student', description='', of_type=<NodeType.FUNCTION: 2>, parent_identifier='examples/StringTypedClass/NodeType.CLASS', path=None, args=('self',), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='enum/Enum/NodeType.CLASS', name='Enum', description='Generic enumeration.\\n\\nDerive from this class to define new enumerations.', of_type=<NodeType.CLASS: 1>, parent_identifier='/enum/NodeType.MODULE', path=None, args=('cls', 'value', 'names'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='builtins/str/NodeType.CLASS', name='str', description=\"str(object='') -> str\\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\\n\\nCreate a new string object from the given object. If encoding or\\nerrors is specified, then the object must expose a data buffer\\nthat will be decoded using the given encoding and error handler.\\nOtherwise, returns the result of object.__str__() (if defined)\\nor repr(object).\\nencoding defaults to sys.getdefaultencoding().\\nerrors defaults to 'strict'.\", of_type=<NodeType.CLASS: 1>, parent_identifier='/builtins/NodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='examples/Person/NodeType.CLASS', name='Person', description='Person is a human that has a name and an age', of_type=<NodeType.CLASS: 1>, parent_identifier='/examples/NodeType.MODULE', path=None, args=('self', 'name', 'age'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='examples/random_function/NodeType.FUNCTION', name='random_function', description='Will output something COMPLETLY random', of_type=<NodeType.FUNCTION: 2>, parent_identifier='/examples/NodeType.MODULE', path=None, args=(), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='Animal/hates/NodeType.FUNCTION', name='hates', description='', of_type=<NodeType.FUNCTION: 2>, parent_identifier='examples/Animal/NodeType.CLASS', path=None, args=('self',), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='examples/Course/NodeType.CLASS', name='Course', description='Course contains information about a specific study direction\\nwith name, year as well as whether it is in the spring or fall', of_type=<NodeType.CLASS: 1>, parent_identifier='/examples/NodeType.MODULE', path=None, args=('self', 'name', 'year', 'spring'), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='dataclasses/dataclass/NodeType.FUNCTION', name='dataclass', description='Returns the same class as was passed in, with dunder methods\\nadded based on the fields defined in the class.\\n\\nExamines PEP 526 __annotations__ to determine fields.\\n\\nIf init is true, an __init__() method is added to the class. If\\nrepr is true, a __repr__() method is added. If order is true, rich\\ncomparison dunder methods are added. If unsafe_hash is true, a\\n__hash__() method function is added. If frozen is true, fields may\\nnot be assigned to after instance creation.', of_type=<NodeType.FUNCTION: 2>, parent_identifier='/dataclasses/NodeType.MODULE', path=None, args=('cls',), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='/dataclasses/NodeType.MODULE', name='dataclasses', description='', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='examples.submodule.classes/FooTesterTen/NodeType.CLASS', name='FooTesterTen', description='', of_type=<NodeType.CLASS: 1>, parent_identifier='examples.submodule/examples.submodule.classes/NodeType.MODULE', path=None, args=(), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='builtins/bool/NodeType.CLASS', name='bool', description='bool(x) -> bool\\n\\nReturns True when the argument x is true, False otherwise.\\nThe builtins True and False are the only two instances of the class bool.\\nThe class bool is a subclass of the class int, and cannot be subclassed.', of_type=<NodeType.CLASS: 1>, parent_identifier='/builtins/NodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='examples.submodule/examples.submodule.classes/NodeType.MODULE', name='examples.submodule.classes', description='', of_type=<NodeType.MODULE: 3>, parent_identifier='examples/examples.submodule/NodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='StringTypedClass/to/NodeType.FUNCTION', name='to', description='', of_type=<NodeType.FUNCTION: 2>, parent_identifier='examples/StringTypedClass/NodeType.CLASS', path=None, args=('self',), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='builtins/object/NodeType.CLASS', name='object', description='The base class of the class hierarchy.\\n\\nWhen called, it accepts no arguments and returns a new featureless\\ninstance that has no instance attributes and cannot be given any.', of_type=<NodeType.CLASS: 1>, parent_identifier='/builtins/NodeType.MODULE', path=None, args=(), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='examples/BareClass/NodeType.CLASS', name='BareClass', description='', of_type=<NodeType.CLASS: 1>, parent_identifier='/examples/NodeType.MODULE', path=None, args=(), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='examples/BareClassExtension/NodeType.CLASS', name='BareClassExtension', description='', of_type=<NodeType.CLASS: 1>, parent_identifier='/examples/NodeType.MODULE', path=None, args=(), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='enum/auto/NodeType.CLASS', name='auto', description='Instances are replaced with an appropriate value in Enum class suites.', of_type=<NodeType.CLASS: 1>, parent_identifier='/enum/NodeType.MODULE', path=None, args=(), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='examples.submodule.classes/foo_ten/NodeType.FUNCTION', name='foo_ten', description='', of_type=<NodeType.FUNCTION: 2>, parent_identifier='examples.submodule/examples.submodule.classes/NodeType.MODULE', path=None, args=(), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='examples/ClassWithHackyDocumentation/NodeType.CLASS', name='ClassWithHackyDocumentation', description='DescriptionDescriptionDescriptionDescriptionDescription', of_type=<NodeType.CLASS: 1>, parent_identifier='/examples/NodeType.MODULE', path=None, args=(), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='examples/StringTypedClass/NodeType.CLASS', name='StringTypedClass', description='', of_type=<NodeType.CLASS: 1>, parent_identifier='/examples/NodeType.MODULE', path=None, args=(), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='builtins/int/NodeType.CLASS', name='int', description=\"int([x]) -> integer\\nint(x, base=10) -> integer\\n\\nConvert a number or string to an integer, or return 0 if no arguments\\nare given.  If x is a number, return x.__int__().  For floating point\\nnumbers, this truncates towards zero.\\n\\nIf x is not a number or if base is given, then x must be a string,\\nbytes, or bytearray instance representing an integer literal in the\\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\\nBase 0 means to interpret the base from the string as an integer literal.\\n>>> int('0b100', base=0)\\n4\", of_type=<NodeType.CLASS: 1>, parent_identifier='/builtins/NodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='examples/examples.submodule/NodeType.MODULE', name='examples.submodule', description='', of_type=<NodeType.MODULE: 3>, parent_identifier='/examples/NodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='FooTesterTen/test/NodeType.FUNCTION', name='test', description='', of_type=<NodeType.FUNCTION: 2>, parent_identifier='examples.submodule.classes/FooTesterTen/NodeType.CLASS', path=None, args=('self',), lines=None)"
            ),
            GenericRepr(
                "Node(identifier='/examples/NodeType.MODULE', name='examples', description='', of_type=<NodeType.MODULE: 3>, parent_identifier=None, path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='examples/examples.foldermodule/NodeType.MODULE', name='examples.foldermodule', description='', of_type=<NodeType.MODULE: 3>, parent_identifier='/examples/NodeType.MODULE', path=None, args=None, lines=None)"
            ),
            GenericRepr(
                "Node(identifier='examples/Animal/NodeType.CLASS', name='Animal', description='Animal(kind: examples.AnimalType, name: str)', of_type=<NodeType.CLASS: 1>, parent_identifier='/examples/NodeType.MODULE', path=None, args=('self', 'kind', 'name'), lines=None)"
            ),
        ]
    ),
    set(
        [
            GenericRepr(
                "Dependency(from_node='examples/Person/NodeType.CLASS', to_node='dataclasses/dataclass/NodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/AnimalType/NodeType.CLASS', to_node='enum/auto/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/StringTypedClass/NodeType.CLASS', to_node='examples/Student/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/Course/NodeType.CLASS', to_node='dataclasses/dataclass/NodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='typing/List/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/AnimalType/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/Animal/NodeType.CLASS', to_node='typing/List/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/Course/NodeType.CLASS', to_node='builtins/bool/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/Student/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='enum/Enum/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/Animal/NodeType.CLASS', to_node='examples/AnimalType/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='builtins/str/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples.submodule/examples.submodule.classes/NodeType.MODULE', to_node='examples.submodule.classes/FooTesterTen/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/Person/NodeType.CLASS', to_node='builtins/int/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/Animal/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/Person/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/Animal/NodeType.CLASS', to_node='builtins/str/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/random_function/NodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/StringTypedClass/NodeType.CLASS', to_node='examples/Course/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/BareClassExtension/NodeType.CLASS', to_node='examples/BareClass/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples.submodule/examples.submodule.classes/NodeType.MODULE', to_node='examples.submodule.classes/foo_ten/NodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/Course/NodeType.CLASS', to_node='builtins/int/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/BareClassExtension/NodeType.CLASS', to_node='builtins/object/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/examples.submodule/NodeType.MODULE', to_node='examples.submodule.classes/FooTesterTen/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/Course/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='dataclasses/dataclass/NodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/examples.submodule/NodeType.MODULE', to_node='examples.submodule/examples.submodule.classes/NodeType.MODULE')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/Animal/NodeType.CLASS', to_node='dataclasses/dataclass/NodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='builtins/bool/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='StringTypedClass/student/NodeType.FUNCTION', to_node='examples/Student/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/AnimalType/NodeType.CLASS', to_node='enum/Enum/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/BareClass/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='builtins/object/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/examples.submodule/NodeType.MODULE', to_node='examples.submodule.classes/foo_ten/NodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/BareClassExtension/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/Student/NodeType.CLASS', to_node='examples/Person/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='StringTypedClass/to/NodeType.FUNCTION', to_node='builtins/type/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='enum/auto/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='Animal/hates/NodeType.FUNCTION', to_node='typing/List/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/Person/NodeType.CLASS', to_node='builtins/str/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/StringTypedClass/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='Animal/hates/NodeType.FUNCTION', to_node='examples/AnimalType/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/ClassWithHackyDocumentation/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/random_function/NodeType.FUNCTION', to_node='builtins/str/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/examples.submodule/NodeType.MODULE')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/StringTypedClass/NodeType.CLASS', to_node='builtins/type/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='builtins/int/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/Student/NodeType.CLASS', to_node='examples/Course/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='StringTypedClass/student/NodeType.FUNCTION', to_node='examples/Course/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='examples/examples.foldermodule/NodeType.MODULE')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/Student/NodeType.CLASS', to_node='dataclasses/dataclass/NodeType.FUNCTION')"
            ),
            GenericRepr(
                "Dependency(from_node='/examples/NodeType.MODULE', to_node='builtins/type/NodeType.CLASS')"
            ),
            GenericRepr(
                "Dependency(from_node='examples/Course/NodeType.CLASS', to_node='builtins/str/NodeType.CLASS')"
            ),
        ]
    ),
)
