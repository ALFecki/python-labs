from serialization_tool.extension.serializators.serialization import Serialization

class XmlSerialization(Serialization):
    def dump(self, obj, file):
        with open(file, 'w') as f:
            f.write(self.dumps(obj))
    
    def dumps(self, obj):
        pass

    def load(self, file):
        with open(file, 'r') as f:
            return self.loads(f.read())
        
    def loads(self, str):
        pass