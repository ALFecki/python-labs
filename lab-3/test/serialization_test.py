from src.serialization_tool.serialization_factory import SerializationFactory
from .utilities_for_test import (
    Test,
    add,
    some_fn,
    _sqrt,
    square_area,
    sum_func,
    clos,
    lambda_func,
    factorial,
    sum_args,
    sum_kwargs,
    sum_args_kwargs, generator, subgenerator, it, generator_expression, E, C, Zalupa
)

json = SerializationFactory.get_serializer("json")
xml = SerializationFactory.get_serializer("xml")

res_json = lambda x: json.loads(json.dumps(x))
res_xml = lambda x: xml.loads(xml.dumps(x))


def test_primitive_types():
    a = 1
    b = 2.5
    c = True
    d = complex(2, 3)
    e = "Hello, World!"
    f = None

    assert a == res_json(a)
    assert a == res_xml(a)
    assert b == res_json(b)
    assert b == res_xml(b)
    assert c == res_json(c)
    assert c == res_xml(c)
    assert d == res_json(d)
    assert d == res_xml(d)
    assert e == res_json(e)
    assert e == res_xml(e)
    assert f == res_json(f)
    assert f == res_xml(f)


def test_iterable():
    l1 = []
    l2 = [1, -2, "something"]
    l3 = [["Hochu 10", 5], False]

    t1 = ()
    t2 = (1, -2, "something")
    t3 = (["Hochu 10", 5], False)
    b = b"wow"

    assert l1 == res_json(l1)
    assert l1 == res_xml(l1)
    assert l2 == res_json(l2)
    assert l2 == res_xml(l2)
    assert l3 == res_json(l3)
    assert l3 == res_xml(l3)

    assert t1 == res_json(t1)
    assert t1 == res_xml(t1)
    assert t2 == res_json(t2)
    assert t2 == res_xml(t2)
    assert t3 == res_json(t3)
    assert t3 == res_xml(t3)
    assert b == res_json(b)
    assert b == res_xml(b)


def test_dict():
    d1 = dict()
    d2 = {1: 2, 3: 4, 5: 6}
    d3 = {("zelenoglazoe", "taksi"): ["ne tormozi"], 1: "ne tormoziii"}

    assert d1 == res_json(d1)
    assert d1 == res_xml(d1)
    assert d2 == res_json(d2)
    assert d2 == res_xml(d2)
    assert d3 == res_json(d3)
    assert d3 == res_xml(d3)


def test_fn():
    assert add(2, 3) == res_json(add)(2, 3)
    assert add(2, 3) == res_xml(add)(2, 3)
    assert _sqrt(64) == res_json(_sqrt)(64)
    assert _sqrt(64) == res_xml(_sqrt)(64)
    assert some_fn(1, 2, 3) == res_json(some_fn)(1, 2, 3)
    assert some_fn(1, 2, 3) == res_xml(some_fn)(1, 2, 3)


def test_class():
    assert Test("Hello").get_title() == res_json(Test)("Hello").get_title()
    assert Test("Hello").get_title() == res_xml(Test)("Hello").get_title()


def test_object():
    assert Test("Hello").get_title() == res_json(Test("Hello")).get_title()
    assert Test("Hello").get_title() == res_xml(Test("Hello")).get_title()


def test_decorator():
    assert square_area(10) == res_json(square_area(10))
    assert square_area(10) == res_xml(square_area(10))

    deser_json = res_json(sum_func)
    deser_xml = res_xml(sum_func)

    assert sum_func(2, 3, 4, 5, 6) == deser_json(2, 3, 4, 5, 6)
    assert sum_func(2, 3, 4, 5, 6) == deser_xml(2, 3, 4, 5, 6)


def test_closure():
    deser_json = res_json(clos)
    deser_xml = res_xml(clos)

    assert type(clos) == type(deser_json)
    assert type(clos) == type(deser_xml)
    assert (clos(2, 3), deser_json(2, 3))
    assert (clos(2, 3), deser_xml(2, 3))


def test_lambda():
    deser_json = res_json(lambda_func)
    deser_xml = res_xml(lambda_func)

    assert type(lambda_func) == type(deser_json)
    assert type(lambda_func) == type(deser_xml)
    assert lambda_func(2) == deser_json(2)
    assert lambda_func(2) == deser_xml(2)


def test_recursion():
    deser_json = res_json(factorial)
    deser_xml = res_xml(factorial)

    assert type(factorial) == type(deser_json)
    assert type(factorial) == type(deser_xml)
    assert factorial(10) == deser_json(10)
    assert factorial(10) == deser_xml(10)


def test_args_kwargs():
    assert sum_args(10, 20, 30) == res_json(sum_args(10, 20, 30))
    assert sum_args(10, 20, 30) == res_xml(sum_args(10, 20, 30))

    assert sum_kwargs(a=10, b=20, c=30) == res_json(sum_kwargs(a=10, b=20, c=30))
    assert sum_kwargs(a=10, b=20, c=30) == res_xml(sum_kwargs(a=10, b=20, c=30))

    assert sum_args_kwargs(1, 2, 3, a=1, b=2, c=3) == res_json(
        sum_args_kwargs(1, 2, 3, a=1, b=2, c=3)
    )

    assert sum_args_kwargs(1, 2, 3, a=1, b=2, c=3) == res_xml(
        sum_args_kwargs(1, 2, 3, a=1, b=2, c=3)
    )


def test_generator():
    deser_json = res_json(generator())
    assert(type(generator()) == type(deser_json))
    assert(sum(generator()) == sum(deser_json))
    deser_xml = res_xml(generator())
    assert(type(generator()) == type(deser_xml))
    assert(sum(generator()) == sum(deser_xml))

def test_generator_function():
    deser_json = res_json(generator)
    assert(type(generator()) == type(deser_json()))
    assert(sum(generator()) == sum(deser_json()))
    deser_xml = res_xml(generator)
    assert(type(generator()) == type(deser_xml()))
    assert(sum(generator()) == sum(deser_xml()))

def test_subgenerator():
    deser_json = res_json(subgenerator())
    assert(type(subgenerator()) == type(deser_json))
    assert(list(subgenerator()) == list(deser_json))
    deser_xml = res_xml(subgenerator())
    assert(type(subgenerator()) == type(deser_xml))
    assert(list(subgenerator()) == list(deser_xml))

def test_generator_expression():
    deser_json = res_json(generator_expression)
    assert(type(generator_expression) == type(deser_json))
    assert(45 == sum(deser_json))


def test_iterator():
    deser_json = res_json(it)
    assert(45 == sum(deser_json))

def test_multiple_inheritance():
    deser_json = res_json(C())
    assert(str(type(C())) == str(type(deser_json)))
    assert(C().info_c() == deser_json.info_c())
    deser_xml = res_xml(C())
    assert(str(type(C())) == str(type(deser_xml)))
    assert(C().info_c() == deser_xml.info_c())

def test_long_inheritance():
    deser_json = res_json(E())
    assert(str(type(E())) == str(type(deser_json)))
    assert(E().info_e() == deser_json.info_e())
    deser_xml = res_xml(E())
    assert(str(type(E())) == str(type(deser_xml)))
    assert(E().info_e() == deser_xml.info_e())

def test_mro():
    assert(str(C.__mro__) == str(res_json(C).__mro__))
    assert(str(E.__mro__) == str(res_json(E).__mro__))
    assert(str(C.__mro__) == str(res_xml(C).__mro__))
    assert(str(E.__mro__) == str(res_xml(E).__mro__))

def test_class_method():
    deser_json = res_json(Zalupa)
    assert(str(Zalupa.get_const) == str(deser_json.get_const))
    assert(Zalupa.get_const() == deser_json.get_const())
    deser_xml = res_xml(Zalupa)
    assert(str(Zalupa.get_const) == str(deser_xml.get_const))
    assert(Zalupa.get_const() == deser_xml.get_const())

def test_static_method():
    deser_json = res_json(Zalupa)
    assert(type(Zalupa.static) == type(deser_json.static))
    assert(Zalupa.static() == deser_json.static())
    deser_xml = res_xml(Zalupa)
    assert(type(Zalupa.static) == type(deser_xml.static))
    assert(Zalupa.static() == deser_xml.static())


def test_property():
    deser_json = res_json(Zalupa)

    h1 = Zalupa(35, 'Python')
    h2 = deser_json(35, 'Python')
    assert(h1.size == h2.size)

    h1.size = 100
    h2.size = 100
    assert(h1.size == h2.size)

    del h2.size
    assert('name after age deletion' == h2._name)
    assert(False == hasattr(h2, 'size'))

    deser_xml = res_xml(Zalupa)

    h1 = Zalupa(35, 'Python')
    h2 = deser_xml(35, 'Python')
    assert(h1.size == h2.size)

    h1.size = 100
    h2.size = 100
    assert(h1.size == h2.size)

    del h2.size
    assert('name after age deletion' == h2._name)
    assert(False == hasattr(h2, 'size'))
