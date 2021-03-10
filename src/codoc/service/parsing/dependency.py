#!/usr/bin/env python3
import builtins
import inspect
import logging
import os
import subprocess
from functools import lru_cache
from typing import FrozenSet, Iterable, List, Optional, Set, Tuple, Type, Callable


from codoc.domain.model import Node, Dependency
from codoc.service.parsing.node import create_node_from_object, get_parent_of_object


from .regex_identifier_extractor import RegexIdentifierExtractor, SourceNotFoundError
from .types import ObjectType
from .utils import is_an_instance, is_builtin, is_not_an_instance

logger = logging.getLogger(__name__)


class UnexpectedBuiltinError(Exception):
    ...


def get_dependency_nodes(
    obj: ObjectType,
) -> FrozenSet[Node]:
    return DependencyInspector(obj).get_dependency_nodes()


def get_dependency_nodes_with_parents(
    obj: ObjectType,
) -> FrozenSet[Node]:
    return DependencyInspector(obj).get_dependency_nodes_and_parents()


def get_dependency_edges(
    obj: ObjectType,
    node_creator_function: Optional[Callable[[ObjectType], Node]] = None,
) -> FrozenSet[Dependency]:
    return DependencyInspector(obj).get_dependencies()

    if is_builtin(obj):
        raise UnexpectedBuiltinError()
    # TODO maybe we should make it depend on the type then.
    if is_an_instance(obj):
        raise TypeError()

    if not node_creator_function:
        node_creator_function = create_node_from_object

    initial_node = node_creator_function(obj)
    module = get_module_of_object(obj)

    identifiers_in_scope = get_identifier_names_in_scope()

    return frozenset(
        Dependency(from_node=initial_node.identifier, to_node=node.identifier)
        for node in _get_dependency_nodes(
            node=node, node_creator_function=node_creator_function
        )
    )


def get_module_of_object(obj: ObjectType):
    return inspect.getmodule(self._obj)


def _get_dependency_nodes(
    node: Node, node_creator_function: Callable[[ObjectType], Node]
) -> Iterable[Node]:
    return (
        node_creator_function(obj)
        for obj in get_dependency_objects(node)
        if obj is not None and is_not_an_instance(obj)
    )


def get_dependency_objects(node: Node) -> Iterable[ObjectType]:
    """
    Returns objects that our object depends on
    """
    return (
        self.get_object_from_module(identifier)
        for identifier in get_referenced_identifier_names(node)
        if identifier not in ["None"]
    )


def get_referenced_identifier_names(self, node: Node) -> Set[str]:
    try:
        return get_referenced_identifier_names_via_regex() - {
            node.name,
            str(True),
            str(False),
        }
    except SourceNotFoundError:
        return {}


def get_referenced_identifier_names_via_regex(obj: ObjectType, node: Node) -> Set[str]:
    return RegexIdentifierExtractor(
        obj,
        node,
        get_identifier_names_in_scope(),
    ).get_identifiers()


class DependencyInspector:
    """
    Extracts dependencies from a given class or function
    """

    def __init__(self, obj: ObjectType):
        if is_builtin(obj):
            raise UnexpectedBuiltinError()
        # TODO maybe we should make it depend on the type then.
        if is_an_instance(obj):
            raise TypeError()

        self._obj = obj
        self._node = create_node_from_object(obj)
        self._module = inspect.getmodule(self._obj)

    def get_dependencies(self) -> FrozenSet[Dependency]:
        return frozenset(
            Dependency(from_node=self._node.identifier, to_node=node.identifier)
            for node in self.get_dependency_nodes()
        )

    def get_dependency_nodes_and_parents(self) -> FrozenSet[Node]:
        """
        Returns a iterable of all the dependencies this class has, as well as the
        parents of each dependency
        """
        return frozenset(
            create_node_from_object(obj)
            for dependency in self.get_dependency_objects()
            if dependency is not None and is_not_an_instance(dependency)
            for obj in recursively_get_parents(dependency) | {dependency}
            if obj is not None
        )

    def get_dependency_nodes(self) -> Iterable[Node]:
        return (
            create_node_from_object(obj)
            for obj in self.get_dependency_objects()
            if obj is not None and is_not_an_instance(obj)
        )

    def get_dependency_objects(self) -> Iterable[ObjectType]:
        """
        Returns objects that our object depends on
        """
        return (
            self.get_object_from_module(identifier)
            for identifier in self.get_referenced_identifier_names()
            if identifier not in ["None"]
        )

    def get_object_from_module(self, identifier: str) -> Optional[ObjectType]:
        if self._module is None:
            raise NotImplementedError(f"{self._obj} has no module")
        try:
            return getattr(builtins, identifier)
        except AttributeError:
            pass
        try:
            return _recursively_get_member_in_object_matching_identifier_name(
                identifier, self._module
            )
        except AttributeError:
            logger.error(
                f"AttributeError when trying to fetch '{identifier}' when analyzing '{self._obj}'"
            )
            raise

    def get_referenced_identifier_names(self) -> Set[str]:
        try:
            return self.get_referenced_identifier_names_via_regex() - {
                self._node.name,
                str(True),
                str(False),
            }
        except SourceNotFoundError:
            return {}

    def get_referenced_identifier_names_via_regex(self) -> Set[str]:
        return RegexIdentifierExtractor(
            self._obj,
            self._node,
            self.get_identifier_names_in_scope(),
        ).get_identifiers()

    def identifier_is_in_scope(self, identifier: str) -> bool:
        return any(
            identifier == idx2 or identifier.startswith(idx2 + ".")
            for idx2 in self.get_identifier_names_in_scope()
        )

    def get_all_used_identifiers_via_ast(self) -> Set[str]:
        return ASTIdentifierExtractor(self._obj).get_identifiers()

    @lru_cache(maxsize=None)
    def get_identifier_names_in_scope(self) -> Set[str]:
        return set(name for name, value in self.get_identifiers_in_scope())

    def get_identifiers_in_scope(self) -> List[Tuple[str, Type]]:
        return inspect.getmembers(self._module) + inspect.getmembers(builtins)


def recursively_get_parents(obj: object) -> Set[ObjectType]:
    parent = get_parent_of_object(obj)
    if parent is None:
        return set()
    else:
        return {parent} | recursively_get_parents(parent)


def _recursively_get_member_in_object_matching_identifier_name(
    identifier: str, current_object: ObjectType
) -> Optional[ObjectType]:
    split_identifier = identifier.split(".")
    if len(split_identifier) == 1:
        try:
            return getattr(current_object, identifier)
        except AttributeError as e:
            return handle_attribute_error_in_object_inspection(
                e, identifier, current_object
            )
    sub_identifier = ".".join(split_identifier[1:])
    try:
        new_object = getattr(current_object, split_identifier[0])
        return _recursively_get_member_in_object_matching_identifier_name(
            sub_identifier, new_object
        )
    except AttributeError as e:
        return handle_attribute_error_in_object_inspection(
            e, split_identifier[0], current_object
        )


def handle_attribute_error_in_object_inspection(
    error: Exception, identifier: str, current_object: ObjectType
) -> Optional[ObjectType]:
    # Handle special cases - i.e subprocess having OS specific parts
    if current_object in [subprocess, os]:
        logger.warning(
            f"Could not fetch `{identifier}` in `{current_object}`. Assuming it was OS specific."
        )
        return current_object
    # TODO make faster
    if current_object in [
        obj for name, obj in inspect.getmembers(builtins)
    ] or identifier in [name for name, obj in inspect.getmembers(builtins)]:
        logger.warning(
            f"Could not fetch `{identifier}` in `{current_object}`. "
            "Assuming that you are shadowing a builtin."
        )
        return None
    raise error
