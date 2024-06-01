class NotificationStrategy:
    def envoyer(self, message):
        raise NotImplementedError

class EmailNotificationStrategy(NotificationStrategy):
    def envoyer(self, message):
        print(f"Notification envoyée par email: {message}")

class SMSNotificationStrategy(NotificationStrategy):
    def envoyer(self, message):
        print(f"Notification envoyée par SMS: {message}")

class NotificationContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def notifier(self, message):
        self.strategy.envoyer(message)
