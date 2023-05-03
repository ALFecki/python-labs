import sys

sys.path.append("..")


from serialization_tool.serialization_factory import SerializationFactory


def add(a, b):
    return a + b


def main():
    json = SerializationFactory.get_serializer("json")
    c = {2: "a", 3: "b"}
    a = 4
    b = 2.5

    # json.dump([a, b, c], "example.json")
    json.dump(add, "example.json")
    print(json.load("example.json")(2, 3))


if __name__ == "__main__":
    main()
