# Example 1 for understanding class and init method
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"\n{self.name} is now sitting.")

    def roll_over(self):
        print(f"\n{self.name} rolled over!")


my_dog = Dog('Will', 5)


print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")

#.... Example 2 for understanding multiple instances
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


my_dog = Dog('Will', 5)

your_dog = Dog('Lucy', 8)

print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")
my_dog.sit()

print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")
your_dog.sit()