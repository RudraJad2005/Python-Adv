# NOTES: __init__ (constructor)

# __init__ runs after the object is created and sets instance state. It returns None.

class User:
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        if age < 0:
            raise ValueError("age cannot be negative")
        self.age = age

if __name__ == "__main__":
    u = User("Rudra", "Jadhav", 19)
    print(u.first_name, u.last_name, u.age)
