class Employee:
    age = 18 #---> This is class attribute
    language = "Python" #---> This is class attribute


hello = Employee() #---> This is object 
hello.language = "JavaScript" # ---> This is instance attribute 

# NOTE: Instence attribute take preferance over class attribute during assignment or retrieval.(Means on running code JavaScript will print in consol)
print(hello.language, hello.age)