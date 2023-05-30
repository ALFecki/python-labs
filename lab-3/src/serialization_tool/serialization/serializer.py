import inspect
import builtins
import re
from .constants import *
from types import CodeType, FunctionType, ModuleType, CellType, MethodType
from pydoc import locate


class Serializer:
    def create_serializer(self, obj):
        if isinstance(obj, (float, int, complex, bool, str, type(None))):
            return self.serialize_type

        if isinstance(obj, (list, tuple, bytes, set, bytearray)):
            return self.serialize_iterable

        if isinstance(obj, dict):
            return self.serialize_dict

        if inspect.isfunction(obj):
            return self.serialize_function

        if inspect.iscode(obj):
            return self.serialize_code

        if isinstance(obj, CellType):
            return self.serialize_cell

        if inspect.isclass(obj):
            return self.serialize_class

        if isinstance(obj, property):
            return self.serialize_property

        if (
            hasattr(obj, "__iter__")
            and hasattr(obj, "__next__")
            and callable(obj.__iter__)
        ):
            return self.serialize_iterator

        if inspect.ismethod(obj):
            return self.serialize_method

        return self.serialize_object

    def serialize(self, obj):
        serializer = self.create_serializer(obj)
        serialized = serializer(obj)
        serialized = tuple((k, serialized[k]) for k in serialized)

        return serialized

    def serialize_type(self, obj):
        result = dict()

        result[TYPE] = (type(obj).__name__,)
        result[VALUE] = str(obj) if isinstance(obj, complex) else obj

        return result

    def serialize_iterable(self, obj):
        result = dict()

        result[TYPE] = type(obj).__name__
        result[VALUE] = [self.serialize(val) for val in obj]

        return result

    def serialize_dict(self, obj: dict):
        result = dict()
        result[TYPE] = type(obj).__name__
        result[VALUE] = [
            [self.serialize(key), self.serialize(value)] for key, value in obj.items()
        ]

        return result

    def serialize_function(self, function_object, _class=None):
        result = dict()
        result[TYPE] = type(function_object).__name__
        result[VALUE] = {
            FUNCTION_ATTRIBUTES[0]: function_object.__name__,
            FUNCTION_ATTRIBUTES[1]: self.serialize_globals(function_object, _class),
            FUNCTION_ATTRIBUTES[2]: self.serialize(function_object.__closure__),
            FUNCTION_ATTRIBUTES[3]: self.serialize(function_object.__defaults__),
            FUNCTION_ATTRIBUTES[4]: self.serialize(function_object.__kwdefaults__),
            FUNCTION_ATTRIBUTES[5]: {
                key: self.serialize(value)
                for key, value in inspect.getmembers(function_object.__code__)
                if key in CODE_ATTRIBUTES
            },
        }

        return result

    def serialize_globals(self, obj, _class=None):
        _globals = dict()

        for key, value in obj.__globals__.items():
            if key not in obj.__code__.co_names:
                continue

            if isinstance(value, ModuleType):
                _globals[f"module {key}"] = self.serialize(key)

            elif inspect.isclass(value):
                if _class and value != _class or not _class:
                    _globals[key] = self.serialize(value)
            elif key == obj.__code__.co_name:
                _globals[key] = self.serialize(obj.__name__)

            else:
                _globals[key] = self.serialize(value)

        return _globals

    def serialize_class(self, obj):
        result = dict()
        result[TYPE] = CLASS
        result["__name__"] = self.serialize(obj.__name__)

        for key, value in obj.__dict__.items():
            if (
                key in NOT_SERIALIZING_CLASS_ATTRIBUTES
                or type(value) in NOT_SERIALIZING_TYPES
            ):
                continue

            if isinstance(obj.__dict__[key], staticmethod):
                result[key] = dict()
                result[key][TYPE] = "staticmethod"
                result[key][VALUE] = {
                    TYPE: "function",
                    VALUE: self.serialize_function(value.__func__, obj),
                }
            elif isinstance(obj.__dict__[key], classmethod):
                result[key] = dict()
                result[key][TYPE] = "classmethod"
                result[key][VALUE] = {
                    TYPE: "function",
                    VALUE: self.serialize_function(value.__func__, obj),
                }

            elif inspect.ismethod(value):
                result[key] = self.serialize_function(value.__func__, obj)

            elif inspect.isfunction(value):
                result[key] = dict()
                result[key][TYPE] = "function"
                result[key][VALUE] = self.serialize_function(value, obj)

            else:
                result[key] = self.serialize(value)

        result["__bases__"] = dict()
        result["__bases__"][TYPE] = "tuple"
        result["__bases__"][VALUE] = [
            self.serialize(item) for item in obj.__bases__ if item != object
        ]
        return result

    def serialize_object(self, obj):
        result = dict()
        result[TYPE] = OBJECT
        result[VALUE] = {
            "__class__": self.serialize(obj.__class__),
            "__vars__": {
                key: self.serialize(value) for key, value in vars(obj).items()
            },
        }

        return result

    def serialize_code(self, obj):
        return {
            TYPE: obj.__name__,
            VALUE: {
                key: self.serialize(value)
                for key, value in inspect.getmembers(obj)
                if key in CODE_ATTRIBUTES
            },
        }

    def serialize_cell(self, obj):
        result = dict()
        result[TYPE] = type(obj).__name__
        result[VALUE] = self.serialize(obj.cell_contents)
        return result

    def serialize_module(self, module):
        ans = dict()
        ans[TYPE] = MODULE_NAME
        ans[VALUE] = re.search(REGEX_TYPE, str(module)).group(1)

        return ans

    def serialize_property(self, obj):
        result = dict()
        result[TYPE] = obj.__name__
        result[VALUE] = {
            "fget": self.serialize(obj.fget),
            "fset": self.serialize(obj.fset),
            "fdel": self.serialize(obj.fdel),
        }
        return result

    def serialize_iterator(self, obj):
        result = dict()
        result[TYPE] = ITERATOR
        result[VALUE] = [self.serialize(item) for item in obj]
        return result

    def serialize_method(self, obj):
        result = dict()
        result[TYPE] = type(obj).__name__
        result[VALUE] = self.serialize_function(obj.__func__)
        return result

    def create_deserializer(self, object_type):
        
        if object_type in TYPES:
            return self.deserialize_type
        
        if object_type == DICTIONARY:
            return self.deserialize_dict
        
        if object_type in ITERABLE_TYPES:
            return self.deserialize_iterable
        
        if object_type in [FunctionType.__name__, MethodType.__name__]:
            return self.deserialize_function
        
        if object_type == CodeType.__name__:
            return self.deserialize_code
        
        if object_type == CellType.__name__:
            return CellType(self.deserialize)
        
        if object_type == CLASS:
            return self.deserialize_class
        
        if object_type in tuple(map(lambda md: md.__name__, METHOD_DECORATORS)):
            return self.deserialize_method
        
        if object_type == property.__name__:
            return self.deserialize_property
        
        if object_type == ITERATOR:
            return self.deserialize_iterator
        
        return self.deserialize_object


    def deserialize(self, obj):
        obj = dict((a, b) for a, b in obj)
        object_type = obj[TYPE]
        if object_type == CellType.__name__:
            return CellType(self.deserialize(obj[VALUE]))
        
        deserializer = self.create_deserializer(object_type)

        if deserializer is None:
            return

        return deserializer(object_type, obj[VALUE])

    def deserialize_type(self, object_type, obj):
        if object_type == TYPES[5]:
            return None
        else:
            return getattr(builtins, obj[TYPE])(obj[VALUE])

    def deserialize_iterable(self, object_type, obj):
        return getattr(builtins, obj[TYPE])(
            self.deserialize(item) for item in obj[VALUE]
        )

    def deserialize_dict(self, object_type, obj: dict):
        result = {}
        for i in obj:
            val = self.deserialize(i[1])
            result[self.deserialize(i[0])] = val

        return result

    def deserialize_function(self, object_type, foo):
        code = self.deserialize_code(foo["__code__"])
        
        _globals = self.deserialize_globals(foo["__globals__"], foo)
        _globals["builtins"] = __import__("builtins")

        closure = self.deserialize(foo[CLOSURE])
        closure = tuple(closure) if closure else tuple()

        result = FunctionType(code=code, globals=_globals, closure=closure)
        result.__globals__.update({result.__name__: result})
        result.__defaults__ = self.deserialize(foo["__defaults__"])
        result.__kwdefaults__ = self.deserialize(foo["__kwdefaults__"])

        return result
        

    def deserialize_globals(self, globs, func):
        result = dict()

        for key, value in globs.items():
            if MODULE in key:
                result[value[VALUE]] = __import__(value[VALUE])

            elif value != func["__name__"]:
                result[key] = self.deserialize(value)

        return result


    def deserialize_object(self, object_type, obj):
        if object_type == "property":
            obj = self.deserialize(obj)
            return property(
                fget=self.deserialize(obj["fget"]),
                fset=self.deserialize(obj["fset"]),
                fdel=self.deserialize(obj["fdel"]),
            )
        obj_dict = self.deserialize_dict(DICTIONARY, obj)
        result = obj_dict[OBJECT_NAME]()

        for key, value in obj_dict[FIELDS_NAME].items():
            result.key = value

        return result

    def deserialize_class(self, object_type, class_dict):
        
        attributes = {member: self.deserialize(value)
                 for member, value in class_dict.items()}

        _class = type(self.deserialize(class_dict["__name__"]),
                   self.deserialize(class_dict["__bases__"]),
                   attributes)

        for value in attributes.values():
            if inspect.isfunction(value):
                value.__globals__.update({_class.__name__: _class})
            elif isinstance(value, (staticmethod, classmethod)):
                value.__func__.__globals__.update({_class.__name__: _class})

        return _class
    
    def deserialize_method(self, object_type, _method):
        return getattr(builtins, object_type)(self.deserialize(_method[VALUE]))


    def deserialize_property(self, object_type, _property):
        return property(fget=self.deserialize(_property[VALUE]["fget"]),
                            fset=self.deserialize(_property[VALUE]["fset"]),
                            fdel=self.deserialize(_property[VALUE]["fdel"]))


    def deserialize_iterator(self, object_type, _iter):
        return iter(self.deserialize(item) for item in _iter[VALUE])
    
    def _unpack_object(self, object_type, obj):
    
        result = object.__new__(self.deserialize(obj["__class__"]))
        result.__dict__ = {key: self.deserialize(value)
                             for key, value in obj["__vars__"].items()}

        return result
    
    def deserialize_code(self, object_type, code):
        return CodeType(*(self.deserialize(code[ATTRIBUTE])
                          for ATTRIBUTE in CODE_ATTRIBUTES)) 

           
