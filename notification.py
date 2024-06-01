"""Module de gestion des notifications."""


class NotificationStrategy:
    """Stratégie de notification de base."""
    def envoyer(self, message):
        """Envoyer la notification."""
        raise NotImplementedError("La méthode envoyer doit"
                                  " être implémentée dans"
                                  " les classes dérivées.")

    def configurer(self, configuration):
        """Configurer la stratégie de notification."""
        raise NotImplementedError("La méthode configurer doit"
                                  " être implémentée dans"
                                  " les classes dérivées.")


class EmailNotificationStrategy(NotificationStrategy):
    """Stratégie de notification par e-mail."""
    def envoyer(self, message):
        """Envoyer la notification par e-mail."""
        print(f"Notification envoyée par email: {message}")

    def configurer(self, configuration):
        """Configurer la stratégie d'e-mail."""
        # Implémentez la logique de configuration spécifique à l'e-mail ici
        raise NotImplementedError("Implémentez la logique de "
                                  "configuration spécifique à l'e-mail ici")

    def envoyer_email(self, destinataire, sujet, contenu):
        """Envoyer un e-mail."""
        # Implémentez la logique d'envoi d'e-mail ici
        raise NotImplementedError("Implémentez la "
                                  "logique d'envoi d'e-mail ici")


class SMSNotificationStrategy(NotificationStrategy):
    """Stratégie de notification par SMS."""
    def envoyer(self, message):
        """Envoyer la notification par SMS."""
        print(f"Notification envoyée par SMS: {message}")

    def configurer(self, configuration):
        """Configurer la stratégie de SMS."""
        # Implémentez la logique de configuration spécifique au SMS ici
        raise NotImplementedError("Implémentez la logique de"
                                  " configuration spécifique au SMS ici")

    def envoyer_sms(self, numero, message):
        """Envoyer un SMS."""
        # Implémentez la logique d'envoi de SMS ici
        raise NotImplementedError("Implémentez la logique d'envoi de SMS ici")


class NotificationContext:
    """Contexte de notification."""
    def __init__(self, strategy):
        """Initialiser le contexte avec une stratégie de notification."""
        self.strategy = strategy

    def notifier(self, message):
        """Notifier en utilisant la stratégie définie."""
        self.strategy.envoyer(message)
