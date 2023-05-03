from serialization_tool.types.json.json import JsonSerialization

# import constants as const


class SerializationFactory:
    def get_serializer(ext: str):
        return JsonSerialization()
        # match ext:
        #     case const.JSON_EXT:
        #         return JsonSerialization()
            
        #     case const.XML_EXT:
        #         pass
            
        #     case _:
        #         print("Unknown type")
                
