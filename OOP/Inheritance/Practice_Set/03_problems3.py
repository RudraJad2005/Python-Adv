"""
# QUESTION: 1
# Abstract Base Class (ABC)
# Make an abstract Repository with save() and get(). Implement MemoryRepository using a dict.
# Save an item and retrieve it, then print the result.

# Solution---1
"""

from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def save(self, item):
        pass

    @abstractmethod
    def get(self, key):
        pass


class MemoryRepository(Repository):
    def __init__(self):
        self._data = {}

    def save(self, item):
        self._data[item["id"]] = item

    def get(self, key):
        return self._data.get(key)


"""
# QUESTION: 2
# Properties with validation
# Create Account with balance property; prevent negative balances in setter. Show it raising an error.

# Solution---2
"""


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
            raise ValueError("balance cannot be negative")
        self._balance = value


"""
# QUESTION: 3
# "Private" attributes via name mangling
# Create SecretBox with __secret; add reveal() that returns it. Print the revealed secret.

# Solution---3
"""


class SecretBox:
    def __init__(self, secret):
        self.__secret = secret  # name-mangled: _SecretBox__secret

    def reveal(self):
        return self.__secret


"""
# QUESTION: 4
# Composition vs Inheritance
# Create Engine with start(); Car composes an Engine and delegates start(). Print the returned string.

# Solution---4
"""


class Engine:
    def start(self):
        return "engine started"


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        return self.engine.start()


if __name__ == "__main__":
    # Q1 demo
    repo = MemoryRepository()
    repo.save({"id": 1, "name": "a"})
    print("Repository get:", repo.get(1))

    # Q2 demo
    acc = Account(10)
    print("Account balance:", acc.balance)
    try:
        acc.balance = -1
    except ValueError as e:
        print("Setter error:", e)

    # Q3 demo
    box = SecretBox("top")
    print("Secret revealed:", box.reveal())

    # Q4 demo
    car = Car(Engine())
    print("Car start:", car.start())
