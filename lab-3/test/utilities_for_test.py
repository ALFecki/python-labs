import math
import pytest


class Test:
    def __init__(self, test_title="class_test"):
        self.test_title = test_title

    def get_title(self):
        return self.test_title


def add(a, b):
    return a + b


def _sqrt(b):
    return math.sqrt(b)


def some_fn(a, b, c):
    a = b + c
    b = a * 12
    return pow(a + b * c, 2)


class Zalupa:
    CONST = "123ABC456"

    def __init__(self, size, name):
        self._size = size
        self._name = name

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @size.deleter
    def size(self):
        del self._size
        self._name = "name after age deletion"

    @classmethod
    def get_const(cls):
        return cls.CONST

    @staticmethod
    def static():
        return 'It is static'


def circle_area(r):
    return math.pi * (r**2)


def decorator1(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs) * 10

    return inner


@decorator1
def square_area(h):
    return h * h


def limit(n):
    def wrapper(func):
        def inner(*args, **kwargs):
            if len(args) + len(kwargs) > n:
                raise ValueError("too much arguments")
            return func(*args, **kwargs)

        return inner

    return wrapper


@limit(5)
def sum_func(*args):
    return sum(args)


def clos(first, second):
    def sum():
        return first + second

    return sum


lambda_func = lambda x: x ** 2

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def sum_args(*args):
    return sum(args)


def sum_kwargs(**kwargs):
    return sum(kwargs.values())


def sum_args_kwargs(*args, **kwargs):
    return sum_args(*args) + sum_kwargs(**kwargs) + \
        sum(args) + sum(kwargs.values())


def generator(start=0, stop=10):
    for i in range(start, stop):
        yield i

generator_expression = (i for i in range(10))


def subgenerator():
    yield from generator()
    yield from generator(5)
    yield from generator(5, 20)

it = iter(list(range(10)))



class A:
    def info_a(self):
        return 'it is a'


class B:
    def info_b(self):
        return 'is is b'


class C(A, B):
    def info_c(self):
        return 'it is c' + self.info_a() + self.info_b()


class D(C):
    def info_d(self):
        return 'it is d'


class E(D):
    def info_e(self):
        return 'it is e' + self.info_a() + \
            self.info_b() + self.info_c() + self.info_d()