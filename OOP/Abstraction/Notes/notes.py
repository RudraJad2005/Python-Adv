# NOTES: Abstraction

# Abstraction hides implementation details and exposes a clear interface.
# In Python, use abc.ABC with @abstractmethod to define required operations.

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class CardPayment(Payment):
    def pay(self, amount: float) -> bool:
        print(f"Charging card: {amount}")
        return True

class UpiPayment(Payment):
    def pay(self, amount: float) -> bool:
        print(f"UPI transfer: {amount}")
        return True

if __name__ == "__main__":
    p: Payment = CardPayment()
    print(p.pay(100))
    p = UpiPayment()
    print(p.pay(50))
