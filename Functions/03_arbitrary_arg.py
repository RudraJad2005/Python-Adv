#---> Arbitrary arguments

# Sometimes you won't know ahead of time how many arguments a function needs to accept. 
# Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling statement.

# .... For example ....

# For example, consider a function that builds a pizza. It needs to accept a number of toppings, but you can’t know ahead of time how many toppings a person will want. 
# The function in the following example has one parameter, *toppings, but this parameter collects as many arguments as the calling line provides:

# ... The asterisk in the parameter name *toppings tells Python to make a tuple called toppings, containing all the values this function recives.

def make_pizza(*toppings):
    """Prints the list of toppings that have been requested"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green pappers', 'extra cheese')

#----> Mixing Positional and Arbitrary Arguments

# You can add several different types of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition.

# .... In the function definition. Python assings the first value it recevies to the parameter size. All other values that come after are stored in the tuple toppings.
def make_pizza(size, *toppings):

    print(f"\nMaking a {size}-inch of pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green pappers', 'extra cheese')