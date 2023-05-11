from src.serialization_tool.serialization_factory import SerializationFactory
import pytest
import math

def test_primitive_types():
    a = 1
    b = 2.5
    c = True
    d = complex(2, 3)
    e = "Hello, World!"
    f = None

    json = SerializationFactory.get_serializer("json")
    json.dump((a, b, c, d, e, f), "test.json")
    assert ((a, b, c, d, e, f) == json.load("test.json"))


def test_iterable():
    l1 = []
    l2 = [1, -2, "something"]
    l3 = [["Hochu 10", 5], False]

    t1 = ()
    t2 = (1, -2, "something")
    t3 = (["Hochu 10", 5], False)
    b = b'wow'

    json = SerializationFactory.get_serializer("json")

    json.dump(l1, "test.json")
    assert(l1 == json.load("test.json"))

    json.dump(l2, "test.json")
    assert(l2 == json.load("test.json"))
    
    json.dump(l3, "test.json")
    assert(l3 == json.load("test.json"))
    
    json.dump(t1, "test.json")
    assert(t1 == json.load("test.json"))
    
    json.dump(t2, "test.json")
    assert(t2 == json.load("test.json"))
    
    json.dump(t3, "test.json")
    assert(t3 == json.load("test.json"))
    
    json.dump(b, "test.json")
    assert(b == json.load("test.json"))

def test_dict():
    d1 = dict()
    d2 = {1: 2, 3: 4, 5: 6}
    d3 = {("zelenoglazoe", "taksi"): ["ne tormozi"], 1: "ne tormoziii"}

    json = SerializationFactory.get_serializer("json")
    json.dump(d1, "test.json")
    assert(d1 == json.load("test.json"))
    json.dump(d2, "test.json")
    assert(d2 == json.load("test.json"))
    json.dump(d3, "test.json")
    assert(d3 == json.load("test.json"))


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
    json = SerializationFactory.get_serializer("json")

    json.dump(test_add, "test.json")
    assert(5 == json.load("test.json")(2, 3))

    json.dump(test_sqrt, "test.json")
    assert(8 == json.load("test.json")(64))

    json.dump(test_some_fn, "test.json")
    assert(34225 == json.load("test.json")(1, 2 ,3))


class Test:
    def __init__(self, test_title = "class_test"):
        self.test_title = test_title

    def get_title(self):
        return self.test_title
    

def test_class():
    json = SerializationFactory.get_serializer("json")

    json.dump(Test, "test.json")
    test = Test("Hello")
    test_response = json.load("test.json")
    result = test_response("Hello")
    assert(result.get_title() == test.get_title())

