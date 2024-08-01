# Question 1) Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. 
# Call the function three times, using a different number of arguments each time.

# ... Soution ...
def sandwich_maker(**items):

    print(f"Your sandwich is placed")
    print(f"{items}")

sandwich_maker(name="Rudra", sandwich=3)
sandwich_maker(bread = "white_bread", topping="tomato, potato")

# Question 2) #Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. 
# It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
# Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly.

def make_car(car__name, car_type, color, sunroof=None):
    final_car = {'car_name': {car__name}, 'car_type': {car_type}, 'color': {color}}
    if sunroof:
        final_car['sun_roof'] = sunroof
    return final_car


client = make_car("BMW M5", "Sidan", "Black")
print(client)