from constants import VALUE
from constants import TYPE
from constants import TYPES
from constants import ITERABLE_TYPES



class Serializer:
    def serialize(self, obj):
        result = {}
        
        pass

    def deserialize(self, obj):
        pass


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
        

            
        

