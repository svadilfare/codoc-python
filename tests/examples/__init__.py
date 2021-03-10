#!/usr/bin/env python3
from dataclasses import dataclass
from typing import List
from enum import Enum, auto

from . import submodule
from . import foldermodule


class BareClass:
    pass


class BareClassExtension(BareClass, object):
    pass


@dataclass
class Person:
    """
    Person is a human that has a name and an age
    """

    name: str
    age: int


@dataclass
class Course:
    """
    Course contains information about a specific study direction
    with name, year as well as whether it is in the spring or fall
    """

    name: str
    year: int
    spring: bool


class StringTypedClass:
    def to(self) -> "StringTypedClass":
        return type(self)()

    def student(self) -> "Student":
        return Student(
            name="Casper", age=99, course=Course(name="Test", year=2020, spring=True)
        )


@dataclass
class Student(Person):
    course: Course


def random_function() -> str:
    """
    Will output something COMPLETLY random
    """
    return "LOL IM SOO RANDOM XDDD"


PYTHON_SCRIPT_USING_TYPING = """
from Typing import List

def foo(x: int) -> List[str]:
  return ["hello"] * x
"""
PYTHON_SCRIPT_USING_INSPECT = """
import inspect

def get_inspect_source_and_module(elm) -> str:

  return inspect.getsource(elm), inspect.getmodulename(elm)
"""


CLASS_INSTANCE = Course("Research Project", 2020, True)


class ClassWithHackyDocumentation:
    """
    No description
    """

    x = 5


ClassWithHackyDocumentation.__doc__ = "Description" * 5


class AnimalType(Enum):
    DOG = auto()
    CAT = auto()
    MICE = auto()


@dataclass
class Animal:
    kind: AnimalType
    name: str

    def hates(self) -> List[AnimalType]:
        return [AnimalType.DOG]
        # TODO uncomment so test fails
        # return [t for t in AnimalType.choices() if t is not self.kind]
