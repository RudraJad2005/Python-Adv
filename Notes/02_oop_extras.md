# OOP Extras — Dunders, ABCs, Mixins, Composition

Concise notes with examples you can run.

## Dunder Methods Cheatsheet

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
```

## Context Manager

```python
class File:
    def __init__(self, path, mode):
        self.path, self.mode = path, mode
    def __enter__(self):
        self.f = open(self.path, self.mode, encoding="utf-8")
        return self.f
    def __exit__(self, exc_type, exc, tb):
        self.f.close()
        return False  # don’t suppress
```

## Abstract Base Classes and Protocols

```python
from abc import ABC, abstractmethod

class Writer(ABC):
    @abstractmethod
    def write(self, text: str) -> int:
        ...
```

Structural typing with Protocols:

```python
from typing import Protocol

class Writable(Protocol):
    def write(self, text: str) -> int: ...
```

## Mixins

- Keep them small and behavior-focused.
- Avoid storing state in mixins; if needed, document expectations clearly.

```python
class ReprMixin:
    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"
```

## Dataclasses

```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
```

## Composition Example

```python
class Cache:
    def get(self, k): ...

class Service:
    def __init__(self, cache: Cache):
        self.cache = cache
    def get_user(self, id):
        return self.cache.get(id)
```
