from serialization_tool.serialization_factory import SerializationFactory
import math


def my_decor(meth):
    def inner(*args, **kwargs):
        print('I am in my_decor')
        return meth(*args, **kwargs)

    return inner


class A:
    x = 10

    @my_decor
    def my_sin(self, c):
        return math.sin(c * self.x)

    @staticmethod
    def stat():
        return 145

    def __str__(self):
        return 'AAAAA'

    def __repr__(self):
        return 'AAAAA'


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def prop(self):
        return self.a * self.b

    @classmethod
    def class_meth(cls):
        return math.pi


class C(A, B):
    pass


ser = SerializationFactory.get_serializer('xml')
#
# var = 15
# var_ser = ser.dumps(var)
# var_des = ser.loads(var_ser)
# print(var_des)
#
C_ser = ser.dumps(C)
C_des = ser.loads(C_ser)

c = C(1, 2)
c_ser = ser.dumps(c)
c_des = ser.loads(c_ser)

print(c_des)
print(c_des.x)
print(c_des.my_sin(10))
print(c_des.prop)
print(C_des.stat())
print(c_des.class_meth())


def f(a):
    for i in a:
        yield i


g = f([1, 2, 3])
print(next(g))
g_s = ser.dumps(g)
g_d = ser.loads(g_s)
print(next(g_d))


def a(x):
    yield x[0]
    x[1] += 2
    yield

def countdown(n):
    print(n)
    if n == 0:
        return         
    else:
        countdown(n - 1) 

lam = lambda x: x ** 2

print(ser.loads(ser.dumps(countdown))(5))
print(ser.loads(ser.dumps(lam))(5))





