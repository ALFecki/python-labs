import inspect
import re
from .constants import *
from types import CodeType, FunctionType, ModuleType, CellType
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
        
        if hasattr(obj, '__iter__') and hasattr(obj, '__next__') and callable(obj.__iter__):
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
            }
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

            if key in NOT_SERIALIZING_CLASS_ATTRIBUTES or type(value) in NOT_SERIALIZING_TYPES:
                continue

            if isinstance(obj.__dict__[key], staticmethod):
                result[key] = dict()
                result[key][TYPE] = "staticmethod"
                result[key][VALUE] = {TYPE: "function", VALUE: self.serialize_function(value.__func__, obj)}
            elif isinstance(obj.__dict__[key], classmethod):
                result[key] = dict()
                result[key][TYPE] = "classmethod"
                result[key][VALUE] = {TYPE: "function", VALUE: self.serialize_function(value.__func__, obj)}

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
        result["__bases__"][VALUE] = [self.serialize(item) for item in obj.__bases__ if item != object]
        return result



    def serialize_object(self, obj):
        
        result = dict()
        result[TYPE] = OBJECT
        result[VALUE] = {
            "__class__": self.serialize(obj.__class__),
            "__vars__": {key: self.serialize(value) for key, value in vars(obj).items()}
        }

        return result

    def serialize_instance(self, obj):
        result = dict()
        result[TYPE] = re.search(REGEX_TYPE, str(type(obj))).group(1)

        result[VALUE] = {}
        members = inspect.getmembers(obj)
        members = [i for i in members if not callable(i[1])]
        for i in members:
            key = self.serialize(i[0])
            val = self.serialize(i[1])
            result[VALUE][key] = val
        result[VALUE] = tuple((k, result[VALUE][k]) for k in result[VALUE])

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
        result[TYPE] =  type(obj).__name__
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
        if object_type == DICTIONARY:
            return self.deserialize_dict
        if object_type == FUNCTION:
            return self.deserialize_function
        if object_type in ITERABLE_TYPES:
            return self.deserialize_iterable
        if object_type == CLASS:
            return self.deserialize_class
        if object_type in TYPES:
            return self.deserialize_type
        if object_type == OBJECT or object_type == "property":
            return self.deserialize_object
        if object_type == MODULE_NAME:
            return self.deserialize_module

    def deserialize(self, obj):
        obj = dict((a, b) for a, b in obj)
        object_type = obj[TYPE]
        deserializer = self.create_deserializer(object_type)

        if deserializer is None:
            return

        return deserializer(object_type, obj[VALUE])

    def deserialize_type(self, object_type, obj):
        if object_type == TYPES[5]:
            return None

        if object_type == TYPES[2] and isinstance(obj, str):
            return obj == "True"

        return locate(object_type)(obj)

    def deserialize_iterable(self, object_type, obj):
        result = []

        for value in obj:
            result.append(self.deserialize(value))

        if object_type == ITERABLE_TYPES[0]:
            return result
        elif object_type == ITERABLE_TYPES[1]:
            result = tuple(result)
        elif object_type == ITERABLE_TYPES[2]:
            result = set(result)
        else:
            result = bytes(result)

        return result

    def deserialize_dict(self, object_type, obj: dict):
        result = {}
        for i in obj:
            val = self.deserialize(i[1])
            result[self.deserialize(i[0])] = val

        return result

    def deserialize_function(self, object_type, foo):
        func = [0] * 4
        code = [0] * 16
        glob = {BUILTINS: __builtins__}

        for i in foo:
            key = self.deserialize(i[0])

            if key == GLOBALS:
                glob_dict = self.deserialize(i[1])
                for glob_key in glob_dict:
                    glob[glob_key] = glob_dict[glob_key]

            elif key == CODE:
                val = i[1][1][1]

                for arg in val:
                    code_arg_key = self.deserialize(arg[0])
                    if code_arg_key != DOC and code_arg_key != "co_linetable":
                        code_arg_val = self.deserialize(arg[1])
                        index = CODE_OBJECT_ARGS.index(code_arg_key)
                        code[index] = code_arg_val

                code = CodeType(*code)
            else:
                index = FUNCTION_ATTRIBUTES.index(key)
                func[index] = self.deserialize(i[1])

        func[0] = code
        func.insert(1, glob)

        ans = FunctionType(*func)
        if ans.__name__ in ans.__getattribute__(GLOBALS):
            ans.__getattribute__(GLOBALS)[ans.__name__] = ans

        return ans

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
        some_dict = self.deserialize_dict(DICTIONARY, class_dict)
        name = some_dict[NAME]
        del some_dict[NAME]

        return type(name, (object,), some_dict)

    def deserialize_module(self, object_type, module_name):
        return __import__(module_name)
