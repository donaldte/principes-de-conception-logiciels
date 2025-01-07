class EmailService:
    def send_email(self, recipient, subject, content):
        print(f"Sending email to {recipient} with subject '{subject}'")

class NotificationManager:
    def __init__(self):
        self.email_service = EmailService()

    def notify(self, recipient, message):
        self.email_service.send_email(recipient, "Notification", message)











# code refactorisé
# 1- interface
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def notify(self, recipient, message):
        pass
    
# 2- service specifiques

class EmailNotificationService(NotificationService):
    def notify(self, recipient, message):
        print(f"Sending email to {recipient} with message: {message}")

class SMSNotificationService(NotificationService):
    def notify(self, recipient, message):
        print(f"Sending SMS to {recipient} with message: {message}")
    

# 3- NotificationManager adapter 

class NotificationManager:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def notify(self, recipient, message):
        self.notification_service.notify(recipient, message)


# 4- Utilisation

# Envoyer une notification par e-mail
email_service = EmailNotificationService()
manager = NotificationManager(email_service)
manager.notify("user@example.com", "This is an email notification")

# Envoyer une notification par SMS
sms_service = SMSNotificationService()
manager = NotificationManager(sms_service)
manager.notify("123-456-7890", "This is an SMS notification")
