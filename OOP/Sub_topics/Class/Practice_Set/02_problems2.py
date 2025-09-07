# QUESTION: 2

# Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user. 
# Create several instances representing different users, and call both methods for each user.

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