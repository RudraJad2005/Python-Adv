# Question 1
# T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. 
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

# Solution---1

def make_shirt(size, text_on_shirt):

    print(f"The size of the shirt is {size} and the text on shirt is {text_on_shirt}")


make_shirt(32, "God is great")
make_shirt(size=32, text_on_shirt="God is great")

# Question 2
# Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

# Solution---2

def make_shirt(size="Large", message="I love python"):
    print(f"You shirt size is {size}, and message is {message}")


make_shirt("small", message="God is great")
make_shirt("medium")

# Question 3 
# Cities: Write a function called describe_city() that accepts the name of a city and its country. 
# The function should print a simple sentence, such as Rudra is in India. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

# Solution----3

def describe_city(city, country="India"):
    print(f"Rudra is in {city} in {country}")


describe_city("Mdarid", country="Spain")
describe_city("Barcelona", country="Spain")
describe_city("Bangalore")
