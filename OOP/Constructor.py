class Employee:
    age = 18 #---> This is class attribute
    language = "Python" #---> This is class attribute
    salary = 1200000

    def __init__(self, name, salary, language): #---> This is called dunder method which is automatically called 
        self.name = name
        self.salary = salary
        self.language = language
        print("Creating an object")

    def getInfo(self):
        print(f"The language is {self.language} and age is {self.age}")

    @staticmethod #---> This is a decorator which don't take self.
    def greet():
        print("Good morning")


hello = Employee("Harry", 1300000, "C++") #---> This is object 
hello.name = "Rudra"
print(hello.age, hello.language, hello.name, hello.salary)