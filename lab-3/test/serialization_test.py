from src.serialization_tool.serialization_factory import SerializationFactory
import pytest
import math

json = SerializationFactory.get_serializer("json")
xml = SerializationFactory.get_serializer("xml")

def test_primitive_types():
    a = 1
    b = 2.5
    c = True
    d = complex(2, 3)
    e = "Hello, World!"
    f = None


    json.dump(a, "test.json")
    assert (a == json.load("test.json"))
    xml.dump(a, "test.xml")
    assert (a == xml.load("test.xml"))
    json.dump(b, "test.json")
    assert (b == json.load("test.json"))
    xml.dump(b, "test.xml")
    assert (b == xml.load("test.xml"))
    json.dump(c, "test.json")
    assert (c == json.load("test.json"))
    xml.dump(c, "test.xml")
    assert (c == xml.load("test.xml"))
    json.dump(d, "test.json")
    assert (d == json.load("test.json"))
    xml.dump(d, "test.xml")
    assert (d == xml.load("test.xml"))
    json.dump(e, "test.json")
    assert (e == json.load("test.json"))
    xml.dump(e, "test.xml")
    assert (e == xml.load("test.xml"))
    json.dump(f, "test.json")
    assert (f == json.load("test.json"))
    xml.dump(f, "test.xml")
    assert (f == xml.load("test.xml"))


def test_iterable():
    l1 = []
    l2 = [1, -2, "something"]
    l3 = [["Hochu 10", 5], False]

    t1 = ()
    t2 = (1, -2, "something")
    t3 = (["Hochu 10", 5], False)
    b = b'wow'

    json.dump(l1, "test.json")
    assert(l1 == json.load("test.json"))
    xml.dump(l1, "test.xml")
    assert(l1 == xml.load("test.xml"))

    json.dump(l2, "test.json")
    assert(l2 == json.load("test.json"))
    xml.dump(l2, "test.xml")
    assert(l2 == xml.load("test.xml"))
    
    json.dump(l3, "test.json")
    assert(l3 == json.load("test.json"))
    xml.dump(l3, "test.xml")
    assert(l3 == xml.load("test.xml"))
    
    json.dump(t1, "test.json")
    assert(t1 == json.load("test.json"))
    xml.dump(t1, "test.xml")
    assert(t1 == xml.load("test.xml"))
    
    json.dump(t2, "test.json")
    assert(t2 == json.load("test.json"))
    xml.dump(t2, "test.xml")
    assert(t2 == xml.load("test.xml"))
    
    json.dump(t3, "test.json")
    assert(t3 == json.load("test.json"))
    xml.dump(t3, "test.xml")
    assert(t3 == xml.load("test.xml"))
    
    json.dump(b, "test.json")
    assert(b == json.load("test.json"))
    xml.dump(b, "test.xml")
    assert(b == xml.load("test.xml"))

def test_dict():
    d1 = dict()
    d2 = {1: 2, 3: 4, 5: 6}
    d3 = {("zelenoglazoe", "taksi"): ["ne tormozi"], 1: "ne tormoziii"}

    json.dump(d1, "test.json")
    assert(d1 == json.load("test.json"))
    xml.dump(d1, "test.xml")
    assert(d1 == xml.load("test.xml"))
    json.dump(d2, "test.json")
    assert(d2 == json.load("test.json"))
    xml.dump(d2, "test.xml")
    assert(d2 == xml.load("test.xml"))
    json.dump(d3, "test.json")
    assert(d3 == json.load("test.json"))
    xml.dump(d3, "test.xml")
    assert(d3 == xml.load("test.xml"))


@pytest.mark.skip
def test_add(a, b):
    return a + b

@pytest.mark.skip
def test_sqrt(b):
    return math.sqrt(b)

@pytest.mark.skip  
def test_some_fn(a, b, c):
    a = b + c
    b = a * 12
    return pow(a + b * c, 2)

def test_fn():

    json.dump(test_add, "test.json")
    assert(test_add(2, 3) == json.load("test.json")(2, 3))
    xml.dump(test_add, "test.xml")
    assert(test_add(2, 3) == xml.load("test.xml")(2, 3))

    json.dump(test_sqrt, "test.json")
    assert(test_sqrt(64) == json.load("test.json")(64))
    xml.dump(test_sqrt, "test.xml")
    assert(test_sqrt(64) == xml.load("test.xml")(64))

    json.dump(test_some_fn, "test.json")
    assert(test_some_fn(1, 2, 3) == json.load("test.json")(1, 2 ,3))
    xml.dump(test_some_fn, "test.xml")
    assert(test_some_fn(1, 2, 3) == xml.load("test.xml")(1, 2, 3))


class Test:
    def __init__(self, test_title = "class_test"):
        self.test_title = test_title

    def get_title(self):
        return self.test_title
    

def test_class():

    json.dump(Test, "test.json")
    test = Test("Hello")
    test_response = json.load("test.json")
    result = test_response("Hello")
    assert(result.get_title() == test.get_title())

    xml.dump(Test, "test.xml")
    test = Test("Hello")
    test_response = xml.load("test.xml")
    result = test_response("Hello")
    assert(result.get_title() == test.get_title())

