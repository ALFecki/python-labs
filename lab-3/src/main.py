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
    b = Test

    xml = SerializationFactory.get_serializer("xml")
    json.dump(c, "test.json")
    print(json.load("test.json"))
    xml.dump(c, "test.xml")
    test = xml.load("test.xml")
    print(test)
    # test = Test("Hello")
    # json.dump(test, "test.json")
    # result = json.load("test.json")
    # json.dump([a, b, c], "example.json")
    # json.dump(Test, "example.json")
    # # print(json.load("example.json"))
    # test = json.load("example.json")
    # some = test("Hello")
    # print(result.get_title())


if __name__ == "__main__":
    main()
