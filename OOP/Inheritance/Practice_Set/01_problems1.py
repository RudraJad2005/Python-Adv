"""
# QUESTION: 1
# Single Inheritance
# Make a base class Animal with a speak() method returning "..." and a child class Dog
# that overrides speak() to return "woof". Create an instance and print the result of speak().

# Solution---1
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Dog(Animal):
    def speak(self):
        return "woof"


"""
# QUESTION: 2
# Multilevel Inheritance
# Create Vehicle -> Car -> ElectricCar where each level adds attributes.
# Use super().__init__ to chain initializers and then print all attributes.

# Solution---2
"""


class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors


class ElectricCar(Car):
    def __init__(self, brand, doors, battery):
        super().__init__(brand, doors)
        self.battery = battery


"""
# QUESTION: 3
# Hierarchical Inheritance
# Make a parent class Shape and two children Square and Rectangle, each implementing area().
# Create instances and print their areas.

# Solution---3
"""


class Shape:
    def area(self):
        raise NotImplementedError


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


if __name__ == "__main__":
    # Q1 demo
    d = Dog("Rex")
    print("Dog says:", d.speak())

    # Q2 demo
    e = ElectricCar("Tesla", 4, 75)
    print("ElectricCar:", e.brand, e.doors, e.battery)

    # Q3 demo
    s = Square(3)
    r = Rectangle(3, 4)
    print("Square area:", s.area())
    print("Rectangle area:", r.area())
