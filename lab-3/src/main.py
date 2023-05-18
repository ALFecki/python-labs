import sys

sys.path.append("..")

from serialization_tool.serialization_factory import SerializationFactory


def add(a, b):
    return a + b


class Test:
    def __init__(self, title="class_test"):
        self.title = title

    def get_title(self):
        return self.title


def main():
    json = SerializationFactory.get_serializer("json")
    c = {2: "a", 3: "b"}
    a = 4
    b = Test()

    xml = SerializationFactory.get_serializer("xml")
    json.dump(b, "test.json")
    # print(json.load("test.json"))
    res = json.load("test.json")
    print(res.get_title())
    # xml.dump(b, "test.xml")
    # test = xml.load("test.xml")
    # print(test.get_title())
    # xml.dump(add, "test.xml")
    # print(xml.load("test.xml")(2, 3))




if __name__ == "__main__":
    main()
