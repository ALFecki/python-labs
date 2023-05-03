import inspect 
import re
from frozendict import frozendict
from .constants import *



class Serializer:

    def create_serializer(obj):
        if isinstance(obj, (float, int, complex, bool, str, type(None))):
            return Serializer.serialize_type
        if isinstance(obj, (list, tuple, bytes)):
            return Serializer.serialize_iterable
        if isinstance(obj, dict):
            return Serializer.serialize_dict
        if inspect.isfunction(obj):
            return Serializer.serialize_function
        if inspect.isclass(obj):
            return Serializer.serialize_class
        if inspect.iscode(obj):
            return serialize_code
        if inspect.ismodule(obj):
            return serialize_module
        if inspect.ismethoddescriptor(obj) or inspect.isbuiltin(obj):
            return serialize_instance
        if inspect.isgetsetdescriptor(obj) or inspect.ismemberdescriptor(obj):
            return serialize_instance
        if isinstance(obj, type(type.__dict__)):  # mappingproxy type
            return serialize_instance

        return serialize_object
    
    def serialize(obj):
        """
        :param obj: object to serialize
        :return: tuple of dicts of tuples..., that can be used to create JSON
        """
        serializer = Serializer.create_serializer(obj)
        serialized = serializer(obj)
        serialized = tuple((k, serialized[k]) for k in serialized)

        return serialized

    def deserialize(self, obj: dict):
        try:
            object_type : str = obj[TYPE]
        except:
            print("Type cannot be found")

        result = object

        if object_type == DICTIONARY:
            result = self.deserialize_dict(obj)
        elif object_type in TYPES:
            result = self.deserialize_type(obj)
        elif object_type in ITERABLE_TYPES:
            result = self.deserialize_iterable(obj)

        return result


    def serialize_type(self, obj):
        
        result = dict()
        result[TYPE] = re.search(REGEX_TYPE, str(type(obj))).group(1)
        result[VALUE] = obj

        return result

    def deserialize_type(self, obj):
        result = object

        if obj[TYPE] == TYPES[0]:
            result = int(obj[VALUE])
        elif obj[TYPE] == TYPES[1]:
            result = float(obj[VALUE])
        elif obj[TYPE] == TYPES[2]:
            result = (obj[VALUE] == "True")
        elif obj[TYPE] == TYPES[4]:
            result = complex(obj[VALUE])
        elif obj[TYPE] == TYPES[5]:
            result = None
        else:
            result = obj[VALUE]

        return result      


    def serialize_iterable(self, obj):
        result = dict()

        for value in obj:
            result[VALUE].append(self.serialize(value))
        
        result[VALUE] = tuple(result[VALUE])
        return result
    
    def deserialize_iterable(self, obj):
        result = []

        for value in obj:
            result.append(self.deserialize(value))

        if obj[TYPE] == ITERABLE_TYPES[0]:
            return result
        elif obj[TYPE] == ITERABLE_TYPES[1]:
            result = tuple(result)
        elif obj[TYPE] == ITERABLE_TYPES[2]:
            result = set(result)
        else:
            result = bytes(result)

        return result

    def serialize_dict(self, obj: dict):
        result = dict()
        result[TYPE] = DICTIONARY
        result[VALUE] = {}
        
        for key, value in obj.items():
            key_result = self.serialize(key)
            value_result = self.serialize(value)

            result[VALUE][key_result] = value_result

        result[VALUE] = tuple((k, result[VALUE][k])
                              for k in result[VALUE])
        
        return result


        
    def deserialize_dict(self, obj: dict):
        result = {}
        if (type(obj[VALUE]) == tuple):
            return result
        
        for key, value in obj[VALUE].items():
            key_result = self.deserialize(key)
            value_result = self.deserialize(value)
            result[key_result] = value_result
        
        return result
    

    def serialize_function(function_object):
        result = dict()
        result[TYPE] = FUNCTION
        result[VALUE] = {}

        members = inspect.getmembers(function_object)
        members = [i for i in members if i[0] in FUNCTION_ATTRIBUTES]
        
        for i in members:
            key = Serializer.serialize(i[0])
        
            if i[0] != CLOSURE:
                value = Serializer.serialize(i[1])
            else:
                value = Serializer.serialize(None)

            result[VALUE][key] = value
            if i[0] == CODE:
                key = Serializer.serialize(GLOBALS)
                result[VALUE][key] = {}
                names = i[1].__getattribute__("co_names")
                
                glob = function_object.__getattribute__(GLOBALS)
                glob_dict = {}
                
                for name in names:
                    if name == function_object.__name__:
                        glob_dict[name] = function_object.__name__
                    elif name in glob and not inspect.ismodule(name) and name not in __builtins__:
                        glob_dict[name] = glob[name]
                
                result[VALUE][key] = Serializer.serialize(glob_dict)

        result[VALUE] = tuple((k, result[VALUE][k]) for k in result[VALUE])
        return result


    def serialize_class(self, obj):
        result = {VALUE: {}}
        members = []
        bases = []

        for base in obj.__bases__:
            if base.__name__ != OBJECT:
                bases.append(base)
        result[VALUE][self.serialize(BASE)] = self.serialize(bases)

        for member in inspect.getmembers(obj):
            if member[0] not in CLASS_ATTRIBUTE_NAMES:
                members.append(member)

        result_data = self.serialize(DATA)

        new_dict = {NAME: obj.__name__}

        for member in members:

            new_dict[member[0]] = member[1]

        result[VALUE][result_data] = self.serialize(new_dict)

        return result
            
def serialize_object(some_object):
    class_obj = type(some_object)
    result = dict()
    result[TYPE] = OBJECT
    result[VALUE] = {}
    result[VALUE][Serializer.serialize(OBJECT_NAME)] = Serializer.serialize(class_obj)
    result[VALUE][Serializer.serialize(FIELDS_NAME)] = Serializer.serialize(some_object.__dict__)
    result[VALUE] = tuple((k, result[VALUE][k]) for k in result[VALUE])

    return result

def serialize_instance(obj):
    result = dict()
    result[TYPE] = re.search(REGEX_TYPE, str(type(obj))).group(1)

    result[VALUE] = {}
    members = inspect.getmembers(obj)
    members = [i for i in members if not callable(i[1])]
    for i in members:
        key = Serializer.serialize(i[0])
        val = Serializer.serialize(i[1])
        result[VALUE][key] = val
    result[VALUE] = tuple((k, result[VALUE][k]) for k in result[VALUE])

    return result


def serialize_code(obj):
    if re.search(REGEX_TYPE, str(type(obj))) is None:
        return None

    ans = dict()
    ans[TYPE] = re.search(REGEX_TYPE, str(type(obj))).group(1)

    ans[VALUE] = {}
    members = inspect.getmembers(obj)
    members = [i for i in members if not callable(i[1])]
    for i in members:
        key = Serializer.serialize(i[0])
        val = Serializer.serialize(i[1])
        ans[VALUE][key] = val
    ans[VALUE] = tuple((k, ans[VALUE][k]) for k in ans[VALUE])

    return ans

def serialize_module(module):
    ans = dict()
    ans[TYPE] = MODULE_NAME
    ans[VALUE] = re.search(REGEX_TYPE, str(module)).group(1)

    return ans
