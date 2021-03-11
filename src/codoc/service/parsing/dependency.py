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
    **kwargs,
) -> FrozenSet[Node]:
    """
    Returns all direct dependencies of the input object
    """
    kwargs = bootstrap_kwargs(kwargs)
    return DependencyInspector(obj, **kwargs).get_dependency_nodes()


def get_dependency_nodes_with_parents(
    obj: ObjectType,
    **kwargs,
) -> FrozenSet[Node]:
    """
    Returns all direct dependencies of the input object
    and the parents of those dependencies
    """
    kwargs = bootstrap_kwargs(kwargs)
    return DependencyInspector(obj, **kwargs).get_dependency_nodes_and_parents()


def get_dependency_edges(
    obj: ObjectType,
    **kwargs,
) -> FrozenSet[Dependency]:
    """
    Returns the edges that reflect the dependencies of the input object
    """
    kwargs = bootstrap_kwargs(kwargs)
    return DependencyInspector(obj, **kwargs).get_dependencies()


def bootstrap_kwargs(kwargs):
    kwargs.setdefault("create_node", create_node_from_object)
    kwargs.setdefault("get_parent", get_parent_of_object)
    kwargs.setdefault("include_external_dependencies", True)
    return kwargs


class DependencyInspector:
    """
    Extracts dependencies from a given class or function
    """

    def __init__(
        self,
        obj: ObjectType,
        create_node: Callable[[ObjectType], Node],
        get_parent: Callable[[ObjectType], ObjectType],
        include_external_dependencies: bool,
    ):
        if is_builtin(obj):
            raise UnexpectedBuiltinError()
        # TODO maybe we should return set obj to the type of obj
        if is_an_instance(obj):
            raise TypeError()

        self._obj = obj
        self.create_node = create_node
        self.get_parent = get_parent
        self._include_external_dependencies = include_external_dependencies
        self._node = create_node(obj)
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
            self.create_node(obj)
            for dependency in self.get_dependency_objects()
            if dependency is not None and is_not_an_instance(dependency)
            for obj in self.recursively_get_parents(dependency) | {dependency}
            if obj is not None
        )

    def get_dependency_nodes(self) -> FrozenSet[Node]:
        return frozenset(
            self.create_node(obj)
            for obj in self.get_dependency_objects()
            if obj is not None
            and is_not_an_instance(obj)
            and (self._include_external_dependencies or self.is_in_module(obj))
        )

    def is_in_module(self, obj: ObjectType) -> bool:
        return obj is not None and (
            obj == self._module or self.is_in_module(self.get_parent(obj))
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
            return set()

    def get_referenced_identifier_names_via_regex(self) -> Set[str]:
        return RegexIdentifierExtractor(
            self._obj,
            self._node.name,
            self.get_identifier_names_in_scope(),
        ).get_identifiers()

    @lru_cache(maxsize=None)
    def get_identifier_names_in_scope(self) -> Set[str]:
        return set(name for name, value in self.get_identifiers_in_scope())

    def get_identifiers_in_scope(self) -> List[Tuple[str, Type]]:
        return inspect.getmembers(self._module) + inspect.getmembers(builtins)

    def recursively_get_parents(self, obj: ObjectType) -> Set[ObjectType]:
        parent = self.get_parent(obj)
        if parent is None:
            return set()
        else:
            return {parent} | self.recursively_get_parents(parent)


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
