#!/usr/bin/env python3
import importlib
import inspect
import logging
from typing import Optional, Tuple

from codoc.domain.model import Node, NodeType
from codoc.service.parsing.utils import is_an_instance
from codoc.service.parsing.types import ObjectType

logger = logging.getLogger(__name__)


def create_node_from_object(obj: ObjectType) -> Node:
    return NodeGenerator(obj).generate()


def get_parent_of_object(obj: ObjectType) -> Node:
    return NodeGenerator(obj).get_parent()


def get_identifier_of_object(obj: ObjectType) -> Node:
    return NodeGenerator(obj).get_identifier()


DEBUG_MODE = True


class UnrecognizedTypeError(Exception):
    def __init__(self, obj: object):
        super().__init__(f"cannot deduce type of `{obj}`")


class NameNotFound(Exception):
    def __init__(self, obj: object):
        super().__init__(f"cannot find the name of `{obj}` ({type(obj)})")


# TODO make into functions
class NodeGenerator:
    """
    NodeGenerator used to extract relevant data from a given class-type.
    """

    def __init__(self, obj: object):
        if obj is None:
            raise ValueError()
        if is_an_instance(obj):
            raise ValueError()
        self._obj = obj

    def generate(self) -> Node:
        return Node(
            identifier=self.get_identifier(),
            name=self._get_name(),
            description=self._get_description(),
            of_type=self._get_type(),
            parent_identifier=self._get_parent_identifier(),
            path=self._get_path(),
            args=self._get_args(),
            lines=self._get_lines(),
        )

    def get_identifier(self) -> str:
        """
        Returns the unique identifier of this object
        """
        # TODO maybe we can use base64 encryption to make it shorter.
        #   Not important tho.
        if DEBUG_MODE:
            parent_name = getattr(self.get_parent(), "__name__", self.get_parent())
            return f"{parent_name}.{self._get_name()}{self._get_type()}"

        hash_value = hex(
            hash(
                hash(self._get_name())
                + hash(self._get_type())
                + hash(self.get_parent())
            )
        )
        if hash_value[0] == "-":
            return "x" + hash_value[3:]

        return hash_value[2:]

    def _get_description(self) -> str:
        return inspect.getdoc(self._obj) or ""

    def _get_args(self) -> Optional[Tuple[str, ...]]:
        try:
            return tuple(inspect.getfullargspec(self._obj).args)
        except TypeError:
            return None

    def _get_path(self) -> Optional[str]:
        return None
        # TODO reenable when we get a relative path, not including home etc.
        # TODO or simply use another node_creator when running tests
        try:
            return inspect.getfile(self._obj)
        except TypeError:
            return None

    def _get_lines(self) -> Optional[Tuple[int, int]]:
        return None
        # TODO reenable when we get a relative path, not including home etc.
        # TODO or simply use another node_creator when running tests
        try:
            file_name = inspect.getfile(self._obj)
        except TypeError:
            return None
        try:
            with open(file_name) as f:
                content = f.read()
                try:
                    source = inspect.getsource(self._obj)
                except OSError:
                    return None
                start = len(content.split(source)[0].split("\n"))
                end = start + len(source.split("\n")) - 1
                return (start, end)
        except (FileNotFoundError, UnicodeDecodeError):
            return None

    def _get_name(self) -> str:
        try:
            return self._obj.__name__
        except AttributeError:
            try:
                return self._obj._name
            except AttributeError:
                try:
                    return self._obj.name
                except AttributeError:
                    raise NameNotFound(self._obj)

    def _get_type(self) -> NodeType:

        # Some of the elements in `typing` are actually a str
        # so we have to check for this first
        # however some of the elements in `types` are also classes
        # so we need to check for types first
        if self._obj is str:
            return NodeType.CLASS

        if inspect.isclass(self._obj):
            return NodeType.CLASS
        if getattr(self._obj, "__module__", "").startswith("typing"):
            return NodeType.CLASS
        if callable(self._obj):
            return NodeType.FUNCTION
        if inspect.ismodule(self._obj):
            return NodeType.MODULE

        # TODO find out if we can make this assumption
        return NodeType.CLASS
        # raise UnrecognizedTypeError(self._obj)

    def _get_parent_identifier(self) -> Optional[str]:
        parent = self.get_parent()

        if parent is None:
            return None

        return NodeGenerator(parent).get_identifier()

    def get_parent(self) -> Optional[object]:
        if inspect.ismodule(self._obj):
            return self._get_outer_module()
        try:
            return self._obj.__parentclass__
        except AttributeError:
            pass
        try:
            return inspect.getmodule(self._obj)
        except AttributeError:
            return None

    # TODO test this function

    def _get_outer_module(self) -> Optional[object]:
        """
        If the current item is a module, then it tries to get the outer module
        """
        outer_module_name = ".".join(self._get_name().split(".")[:-1])
        if outer_module_name == "":
            return None
        outer_module = importlib.import_module(outer_module_name)

        return outer_module
