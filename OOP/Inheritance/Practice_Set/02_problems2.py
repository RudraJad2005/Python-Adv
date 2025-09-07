"""
# QUESTION: 1
# Multiple Inheritance + Mixins
# Create LoggerMixin (log) and SerializerMixin (serialize) and a class C that
# inherits from A and B (both from a Base with cooperative __init__).
# Use super() properly so all initializers run exactly once according to MRO.

# Solution---1
"""


class LoggerMixin:
    def log(self, msg):
        return f"[LOG] {msg}"


class SerializerMixin:
    def serialize(self):
        return self.__dict__.copy()


class Base:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_inited = True


class A(Base):
    def __init__(self, a, *args, **kwargs):
        self.a = a
        super().__init__(*args, **kwargs)


class B(Base):
    def __init__(self, b, *args, **kwargs):
        self.b = b
        super().__init__(*args, **kwargs)


class C(A, B, LoggerMixin, SerializerMixin):
    def __init__(self, a, b, c):
        super().__init__(a=a, b=b)
        self.c = c


if __name__ == "__main__":
    obj = C(1, 2, 3)
    from inspect import getmro
    print("MRO:", getmro(C))
    print("log():", obj.log("hello"))
    print("serialize():", obj.serialize())
    print("base_inited:", obj.base_inited)
