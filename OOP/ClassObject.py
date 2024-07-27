class Employee:
    age = 18 #---> This is class attribute
    language = "Python" #---> This is class attribute


hello = Employee() #---> This is object 
hello.name = "Harry" # ---> This is instance attribute or object attribute
print(hello.name, hello.age, hello.language)

rudra = Employee()
rudra.name = "Rudra"
print(rudra.name, rudra.age, rudra.language)

# Here name is object attribute and age, language is class attribute