class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

class FreePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        if amount > 0:
            raise ValueError("Free payments must have an amount of zero")
        print("Processing free payment")


# utliisation
def handle_payment(processor: PaymentProcessor, amount):
    processor.process_payment(amount)

# Paiement classique
paid_processor = PaymentProcessor()
handle_payment(paid_processor, 100)  # Processing payment of $100

# Paiement gratuit
free_processor = FreePaymentProcessor()
handle_payment(free_processor, 100)  # ValueError: Free payments must have an amount of zero











# Code Refactorisé :

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class PaidPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        if amount <= 0:
            raise ValueError("Paid payments must have a positive amount")
        print(f"Processing payment of ${amount}")

class FreePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        if amount != 0:
            raise ValueError("Free payments must have an amount of zero")
        print("Processing free payment")



def handle_payment(processor: PaymentProcessor, amount):
    processor.process_payment(amount)

# Paiement classique
paid_processor = PaidPaymentProcessor()
handle_payment(paid_processor, 100)  # Processing payment of $100

# Paiement gratuit
free_processor = FreePaymentProcessor()
handle_payment(free_processor, 0)  # Processing free payment
