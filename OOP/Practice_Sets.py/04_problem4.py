class Calculator:

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square of the number {self.n} is {self.n * self.n}")
    def cube(self):
        print(f"Square of the number {self.n} is {self.n * self.n * self.n}")
    def square_root(self):
        print(f"Square of the number {self.n} is {self.n **1/2}")
    
    @staticmethod
    def hello():
        print("Hello, world!")

a = Calculator(4)
a.square()
a.cube()
a.square_root()
a.hello()