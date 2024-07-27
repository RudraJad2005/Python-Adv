from random import randint

class Train:
    a = 10

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked to train no: {self.trainNo} frin {fro} to {to}")

    def getStatus(self):
        print(f"Train No: is running on time {self.trainNo}")

    def getFare(self, fro, to):
        print(f"Ticket fair in train no: {self.trainNo} frin {fro} to {to} is {randint(222, 555)}")


user = Train(12345678910)

user.book("Gujarat", "Delhi")
user.getStatus()
user.getFare("Gujarat", "Delhi")