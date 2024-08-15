# Example 1 for understanding class and init method
class Dog:

    def __init__(self, name, age):# -----> This is called an __init__() method. This method has two leading underscores and two trailing underscores.
        # ---> We defined init method to have three parameters: self, name, age. The self paramater is required in __init__() method, and it must come first, before the other parameters 
        # -----> The two variables defined in the body of the __init__() method each have the prefix self. Any variable prefixed with self is available to every method in the class, and we'll also be able to access these variables through any instances created from the class.
        self.name = name # -------> The self.name = name takes the value associated with the prarameter name and assigns it to the variable name, which is then attached to the instance begin created.
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

print(f"My dog's name is {your_dog.name}")
print(f"My dog's age is {your_dog.age}")
your_dog.sit()


# Example for understanding classes and instances 

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    
    def get_descriptive_name(self):

        long_name = f"{self.model} {self.make} {self.year}"
    
        return long_name.title()
    

car_name = Car("BMW", "M5", 2022) # Created an instance of class Car

print(car_name.get_descriptive_name())
