# This is a function which having 2 parameters, when function describe_pet calls two agruments are passed.

def describe_pet(animal_type, pet_name):

    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} name is {pet_name}.")

describe_pet('hamster', 'harry')
describe_pet('Willie', 'Dog')

# Keyword Arguments:- Keyword argument is a name-value pair that you pass to a function.
#In keyword argument order dosen't matter. But be sure to use the exact name of the praramaters in the function.

def describe_pet(animal_type, pet_name):

    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} name is {pet_name}.")

describe_pet(animal_type="hamster", pet_name='harry')

