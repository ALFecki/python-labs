from ..serialization import Serialization
from .utilities import to_xml

class XmlSerialization(Serialization):
    def dump(self, obj, file):
        with open(file, 'w') as f:
            f.write(self.dumps(obj))
    
    def dumps(self, obj):
        return to_xml(self.serializer.serialize(obj))


    def load(self, file):
        with open(file, 'r') as f:
            return self.loads(f.read())
        
    def loads(self, str):
        pass