# This is a module that contains a function named make_pizza()

def make_pizza(size, *toppings):

    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")