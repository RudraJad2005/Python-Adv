# NOTES: Decorators

# What is a decorator?
# - A function that takes another function and returns a new function.
# - Used for logging, timing, auth checks, caching, etc.

# Basic function decorator

def log_calls(fn):
    def wrapper(*args, **kwargs):
        print(f"calling {fn.__name__} with", args, kwargs)
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} returned", result)
        return result
    return wrapper

# Usage
@log_calls
def add(x, y):
    return x + y

# Preserving metadata (name, docstring)
from functools import wraps

def safe_divide(fn):
    @wraps(fn)
    def inner(a, b):
        if b == 0:
            print("cannot divide by zero")
            return None
        return fn(a, b)
    return inner

@safe_divide
def divide(a, b):
    """Divide a by b"""
    return a / b

# Method decorators: staticmethod, classmethod, property
class Math:
    @staticmethod
    def pi():
        return 3.14159

    @classmethod
    def from_unit(cls):
        return cls()

class Account:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("negative not allowed")
        self._balance = value

if __name__ == "__main__":
    add(2, 3)
    print(divide(8, 2))
    print(divide(1, 0))
    print(Math.pi())
    acc = Account(10)
    print(acc.balance)
