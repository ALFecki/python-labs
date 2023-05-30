import sys

sys.path.append("..")

from serialization_tool.serialization_factory import SerializationFactory
import unittest
import inspect
from pprint import pprint
from serializer_Konchik import JsonSerializer

def add(a, b):
    return a + b


class Test1:
    @property
    def func():
        return 2


class Test:
    def __init__(self, title="class_test"):
        self.title = title

    def get_title(self):
        return self.title


class Human:
    CONST = '123ABC456'

    def __init__(self, age, name):
        self._age = age
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @age.deleter
    def age(self):
        del self._age
        self._name = 'name after age deletion'

json = SerializationFactory.get_serializer("json")
alias = lambda x: json.loads(json.dumps(x))

def test_property():
    deserialized = alias(Human)
    h1 = Human(18, 'Denis')
    h2 = deserialized(18, 'Denis')
    assert(h1.age == h2.age)
    h1.age *= 2
    h2.age *= 2
    print(type(h2))
    assert(h1.age ==  h2.age)

    print('123123123131',type(h2.__dir__),'123123123123')

    pprint(inspect.getmembers(h2))
    del h2.age
    assert('name after age deletion' == h2._name)

def main():

    # test1 = Test1()
    # json.dump(Test1.func, "test.json")
    # test = json.load("test.json")
    # test_property()

    c = {2: "a", 3: "b"}
    # a = 4
    b = Test
    xml = SerializationFactory.get_serializer("xml")

    serializer = JsonSerializer()
    serializer.dump(b, open('test1.json', 'w'))
    a = 1
    # b = 2.5
    c = True
    d = complex(2, 3)
    e = "Hello, World!"
    f = None

    json.dump(a, "test.json")
    assert (a == json.load("test.json"))
    xml.dump(a, "test.xml")
    assert (a == xml.load("test.xml"))
    json.dump(b, "test.json")
    print(b)
    print(json.load('test.json'))
    assert (b == json.load("test.json"))
    xml.dump(b, "test.xml")
    assert (b == xml.load("test.xml"))
    # json.dump(c, "test.json")
    # assert (c == json.load("test.json"))
    # xml.dump(c, "test.xml")
    # assert (c == xml.load("test.xml"))
    # json.dump(d, "test.json")
    # assert (d == json.load("test.json"))
    # xml.dump(d, "test.xml")
    # assert (d == xml.load("test.xml"))
    # json.dump(e, "test.json")
    # assert (e == json.load("test.json"))
    # xml.dump(e, "test.xml")
    # assert (e == xml.load("test.xml"))
    # print(xml.load("test.xml"))
    # json.dump(f, "test.json")
    # assert (f == json.load("test.json"))
    # xml.dump(f, "test.xml")
    # assert (f == xml.load("test.xml"))


if __name__ == "__main__":
    main()
