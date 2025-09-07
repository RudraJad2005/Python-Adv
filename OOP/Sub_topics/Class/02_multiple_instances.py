#.... Example 2 for understanding multiple instances

# You can create as many instances from a class as you need.

# In this example we created a dog named Willie and a dog named Lucy.
# Each dog is a separate instance with its own set of attributes, capable of the same set of actions:
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

print(f"My dog's name is {your_dog.name}")
print(f"My dog's age is {your_dog.age}")
your_dog.sit()