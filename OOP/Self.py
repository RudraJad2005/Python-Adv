class Employee:
    age = 18 #---> This is class attribute
    language = "Python" #---> This is class attribute

    def getInfo(self):
        print(f"The language is {self.language} and age is {self.age}")

    @staticmethod #---> This is a decorator which don't take self.
    def greet():
        print("Good morning")


hello = Employee() #---> This is object 
hello.language = "JavaScript"
hello.getInfo()
hello.greet()
print(hello.language)