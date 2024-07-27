# Making an Argument/Parameter optional 

# Here we made middle_name parameter as an optional 
def get_formatted_name(first_name, last_name, middle_name=""):

    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('Rudra', 'jadhav')
print(musician)

musician = get_formatted_name('Rudra', 'Jadhav', 'Deepak')
print(musician)

# Returning a Dictionary

def build_person(first_name, last_name):
    """Return a dictionary of information abouta person"""
    person =  {'first_name': first_name, 'last_name': last_name}
    return person

musician = build_person('Rohan', 'Rohan Roro Robinson')
print(musician)

# In below example you can add age parameter as an option in a funnction.

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information abouta person"""
    person =  {'first_name': first_name, 'last_name': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('Rohan', 'Rohan Roro Robinson', age=18)
print(musician)