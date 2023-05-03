from serialization_tool.types.json.json import JsonSerialization

from .constants import *


class SerializationFactory:
    def get_file_extension(ext: str):
        return JsonSerialization()

        match ext:
            case constants.JSON_EXT:
                return JsonSerialization()
            case constants.XML_EXT:
                pass
            case _:
                pass
