#    Overriding methods from the parent class 

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

    def fill_gas_tank(self):
        print("Filling the gas tank...")


class ElecticCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40 


    def fill_gas_tank(self): # -----> This method overrides the above parent class method.
        print("This car dosen't have gas tank.")


my_leaf = ElecticCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.fill_gas_tank()
