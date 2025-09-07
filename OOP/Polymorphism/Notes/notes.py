# NOTES: Polymorphism

# Polymorphism allows different classes to be used through the same interface.
# In Python, duck typing and ABCs both enable polymorphism.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

class Dog(Animal):
    def speak(self) -> str:
        return "woof"

class Cat(Animal):
    def speak(self) -> str:
        return "meow"

# Duck typing example
class Human:
    def speak(self) -> str:
        return "hello"

if __name__ == "__main__":
    for obj in [Dog(), Cat(), Human()]:
        print(obj.speak())
