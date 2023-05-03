
OBJECT_TYPE_REGEX = "\'([\w\W]+)\'"
REGEX_TYPE = r"\'(\w+)\'"

TYPE = "TYPE"
VALUE = "VALUE"
CLASS = "class"
OBJECT = "object"
DICTIONARY = "dict"
FUNCTION = "function"
BASE = "base"
DATA = "data"

NAME = "__name__"
CLOSURE = "__closure__"
GLOBALS = "__globals__"
OBJECT_NAME = "__object_type__"
FIELDS_NAME = "__fields__"
MODULE_NAME = "__module__name__"

CODE = "code"
MODULE = "module"

TYPES = [
    "int",
    "float",
    "bool",
    "str",
    "complex",
    "NoneType"
]

ITERABLE_TYPES = [
    "list",
    "tuple",
    "set",
    "bytes"
]

FUNCTION_ATTRIBUTES = [
    "__code__",
    "__name__",
    "__defaults__",
    "__closure__"
]

CLASS_ATTRIBUTE_NAMES = ["__class__",
                         "__doc__",
                         "__getattribute__",
                         "__new__",
                         "__setattr__"
]