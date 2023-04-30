import inspect
from frozendict import frozendict
from .constants import VALUE, TYPE, TYPES, ITERABLE_TYPES, DICTIONARY



class Serializer:
    def serialize(self, obj):
        result = {}

        if inspect.isclass(obj):
            pass
        else:
            object_type = type(obj)

            if object_type == dict:
                result = self.serialize_dict(obj)
            elif isinstance(obj, (int, float, bool, complex, str, type(None))) or obj is None:
                result = self.serialize_type(obj)
            elif object_type == list or object_type == tuple or object_type == set or object_type == bytes:
                result = self.serialize_iterable(obj)

            # result[TYPE] = pass

            return frozendict(result)

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
        return {VALUE: str(obj)}

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
        result = {VALUE: []}

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
        result = {VALUE: {}}
        
        for key, value in obj.items():
            key_result = self.serialize(key)
            value_result = self.serialize(value)

            result[VALUE][key_result] = value_result
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
        

            
        

