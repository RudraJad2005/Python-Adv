# NOTE:- When you create a child class , the parent class must be in the same file as the child class.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):

        long_name = f"{self.model} {self.make} {self.year}"
    
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} on it.")

    def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:

            self.odometer_reading = mileage
        else:
            print("You con't roll back an odometer.")


    def increment_odometer(self, miles):
        self.odometer_reading += miles

# The name of the parent class must be in parentheses in the definition of a child class.

class ElecticCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year) # -----> This super() function is a spectial function that allows you to call a method from the parent class -
                                            # -----> This line tells python to call the __init__() method  from Car, which gives an ElecticCar instance all the attributes defined in that method.

my_leaf = ElecticCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())