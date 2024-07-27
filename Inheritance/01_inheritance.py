class Employee:
    company = "ITC"
    name = "Rudra"
    salary = 1500000
    def show(self):
        print(f"Name of this employee is {self.name} and company is {self.company}")

class Coder:
    languages = "Python"

    def language(self):
        print(f"Language of this employee is {self.languages}")

class Programmer(Employee, Coder):
    company = "ITC Info tech"

    def showLanguage(self):
        print(f"The name is {self.company} and the language is {self.languages} and salary is {self.salary}")

a = Employee()
b = Programmer()

b.show()
b.language()
b.showLanguage()