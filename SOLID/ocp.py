class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "PayPal":
            print(f"Processing PayPal payment of ${amount}")
        elif payment_type == "Stripe":
            print(f"Processing Stripe payment of ${amount}")
        elif payment_type == "MobileMoney":
            print(f"Processing Mobile Money payment of ${amount}")
        else:
            raise ValueError("Unsupported payment type")











# correct code 

from abc import ABC, abstractmethod

# Classe abstraite
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Sous-classe pour PayPal
class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Sous-classe pour Stripe
class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Stripe payment of ${amount}")

# Sous-classe pour Mobile Money
class MobileMoneyProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Mobile Money payment of ${amount}")
