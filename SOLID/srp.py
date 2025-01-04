class InvoiceManager:
    def calculate_total(self):
        # Logique pour calculer le total
        pass

    def save_to_database(self):
        # Logique pour sauvegarder la facture dans la base de données
        pass

    def send_invoice_email(self):
        # Logique pour envoyer la facture par email
        pass







# correct code

class InvoiceCalculator:
    def calculate_total(self, items):
        total = sum(item['price'] * item['quantity'] for item in items)
        return total

class InvoiceStorage:
    def save_to_database(self, invoice):
        # Sauvegarde dans la base de données
        print("Invoice saved to database.")

class EmailSender:
    def send_email(self, recipient, subject, content):
        # Logique pour envoyer un email
        print(f"Email sent to {recipient}")
