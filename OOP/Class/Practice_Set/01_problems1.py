# QUESTION: 1 
# Make a class called Restaurant. The init() method for Restaurant should store two attributes: a restaurant_name and a dish_type. 
# Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods


class Restaurant:
    def __init__(self, restaurant_name, dish_type):
        self.restaurant_name = restaurant_name
        self.dish_type = dish_type
    
    def describe_restaurant(self):
        print(f"Your fav restaurant name is: {self.restaurant_name} and your fav dish is: {self.dish_type}")

    def open_restaurant(self):
        print(f"Your fav restaurant {self.restaurant_name} is: OPEN")

# Creating instances 
restaurant = Restaurant('MacDonald', "Ckicken nugget's")
your_fav_restaurant = Restaurant('Pizza Hut', 'Cheese Pizza')

# Accessing attributes
print(restaurant.restaurant_name)
print(restaurant.dish_type)

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

your_fav_restaurant.describe_restaurant()
your_fav_restaurant.open_restaurant()


# QUESTION: 2
class User:
    def __init__(self, first_name, last_name, DOB, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.DOB = DOB
        self.email = email
        self.password = password

    def describe_user(self):
        print(f"User Name: {self.first_name}\n Last Name: {self.last_name}\n Date of Birth: {self.DOB}\n Your email: {self.email}\n Your passward: {self.password}")


make_user = User('Rudra', 'Jadhav', '13/08/2005', 'rudrajad@gmail.com', 'YOYOBUNTAY :)')

make_user.describe_user()
