# Inheritance — Types and Patterns

This note summarizes inheritance patterns in Python with minimal examples.

## Types of Inheritance

- Single: one parent → one child
- Multilevel: A → B → C chain
- Hierarchical: one parent → many children
- Multiple: class inherits from multiple parents
- Hybrid: combination (e.g., multiple + multilevel). Python uses C3 linearization for MRO.

### Single
```python
class Animal: ...
class Dog(Animal): ...
```

### Multilevel
```python
class A: ...
class B(A): ...
class C(B): ...
```

### Hierarchical
```python
class Shape: ...
class Square(Shape): ...
class Circle(Shape): ...
```

### Multiple + MRO (cooperative)
```python
class Base:
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)

class A(Base):
    def __init__(self, a, *args, **kw):
        self.a = a
        super().__init__(*args, **kw)

class B(Base):
    def __init__(self, b, *args, **kw):
        self.b = b
        super().__init__(*args, **kw)

class C(A, B):
    def __init__(self, a, b):
        super().__init__(a=a, b=b)  # follows MRO
```

Tip: use super() in every class in the diamond and accept/pass on *args, **kwargs.

## Method Resolution Order (MRO)

- C3 linearization decides which parent is called first.
- Get it via `Class.__mro__` or `inspect.getmro(Class)`.

## Overriding and super()

- Overriding: child defines method with same name; parent's version is shadowed.
- Call parent selectively: `super().method(...)`.

```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        base = super().speak()
        return base + " woof"
```

## `__init__` constructor and `super().__init__`

- `__init__` initializes instance state; it returns None.
- Always call `super().__init__()` in subclass `__init__` if parent has state or when using multiple inheritance.
- In multiple inheritance, make `__init__` cooperative:
  - accept `*args, **kwargs`
  - set own attrs
  - call `super().__init__(*args, **kwargs)`

## Decorators (functions and classes)

- Function decorator wraps a function; class decorator wraps a class.

```python
def log_calls(fn):
    def wrapper(*a, **kw):
        print("calling", fn.__name__)
        return fn(*a, **kw)
    return wrapper

@log_calls
def add(x, y):
    return x + y
```

- Method decorators: `@classmethod`, `@staticmethod`, `@property`.

```python
class Util:
    @staticmethod
    def pi():
        return 3.14159

    @classmethod
    def from_str(cls, s):
        return cls()

class Account:
    def __init__(self, balance=0):
        self._balance = 0
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("negative")
        self._balance = value
```

## Attributes and Encapsulation

- Public: no underscore (normal usage)
- Protected (by convention): single underscore `_attr` — internal use
- "Private" (name-mangling): double underscore `__attr` → `_ClassName__attr`
- Use properties to enforce invariants.

```python
class Person:
    def __init__(self, name):
        self.name = name      # public
        self._token = None    # protected-by-convention
        self.__secret = "x"  # name-mangled
```

Access control is by convention; Python doesn’t enforce strict privacy. Name-mangling helps avoid accidental override in subclasses.

## Composition vs Inheritance

Prefer composition when you need behavior reuse without tight type coupling.

```python
class Engine:
    def start(self):
        return "engine"

class Car:
    def __init__(self, engine):
        self.engine = engine
    def start(self):
        return self.engine.start()
```

## Extras you should know

- Dunder methods: `__repr__`, `__str__`, `__eq__`, `__len__`, `__iter__`, `__enter__/__exit__` (context managers)
- Abstract Base Classes (`abc.ABC`) for contracts
- Mixins: narrow, reusable units (no state ideally)
- Dataclasses: auto-generate `__init__`, `__repr__`, comparisons
- `@functools.cached_property` for expensive computed attrs
- `typing.Protocol` for structural subtyping (duck typing)
