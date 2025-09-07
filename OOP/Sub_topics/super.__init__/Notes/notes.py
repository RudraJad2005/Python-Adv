# NOTES: super()

# super() calls the next method in the MRO for the current class.
# Use it to extend behavior and to cooperate across multiple inheritance.

class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        base = super().speak()
        return base + " woof"

# Cooperative multiple inheritance
class Base:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base = True

class A(Base):
    def __init__(self, a, *args, **kwargs):
        self.a = a
        super().__init__(*args, **kwargs)

class B(Base):
    def __init__(self, b, *args, **kwargs):
        self.b = b
        super().__init__(*args, **kwargs)

class C(A, B):
    def __init__(self, a, b):
        super().__init__(a=a, b=b)

if __name__ == "__main__":
    print(Dog().speak())
    c = C(1, 2)
    print(c.a, c.b, c.base)
