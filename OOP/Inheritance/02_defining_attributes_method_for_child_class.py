# Defining attribute and methods for the child class

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


class ElecticCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40 # ---------> This attibute will be assoicated with all instances created from the ElecticCar class but won't be associated with any instances of Car.
                               # ---------> We also add a method called describe_battery() that prints information about the battery. 
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")


my_leaf = ElecticCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()

# There's no limit to hou much you can specialize the ElectricCar class.