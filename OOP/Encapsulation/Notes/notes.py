# NOTES: Attributes and Encapsulation

# Attribute types by convention:
# - public: name
# - protected (convention): _name
# - "private" (name-mangled): __name -> _ClassName__name
# Use properties for validation.

class Person:
    def __init__(self, name, age):
        self.name = name          # public
        self._token = None        # protected (convention)
        self.__ssn = "hidden"     # name-mangled
        self._age = 0
        self.age = age            # go through setter

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("age cannot be negative")
        self._age = value

    def reveal_secret(self):
        return self.__ssn

if __name__ == "__main__":
    p = Person("Rudra", 19)
    print(p.name, p.age)
    print(p.reveal_secret())
    # print(p.__ssn)  # AttributeError
    print(getattr(p, "_Person__ssn"))  # not recommended
