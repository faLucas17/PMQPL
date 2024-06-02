"""Module de gestion des notifications."""

from abc import ABC, abstractmethod


class NotificationStrategy(ABC):
    """Stratégie de notification de base."""

    @abstractmethod
    def envoyer(self, message):
        """Envoyer la notification."""
        pass

    def configurer(self, configuration):
        """Configurer la stratégie de notification."""
        raise NotImplementedError(
            "Implémentez la logique de configuration spécifique ici"
        )


class EmailNotificationStrategy(NotificationStrategy):
    """Stratégie de notification par e-mail."""

    def envoyer(self, message):
        """Envoyer la notification par e-mail."""
        print(f"Notification envoyée par email: {message}")

    def configurer(self, configuration):
        """Configurer la stratégie d'e-mail."""
        raise NotImplementedError(
            "Implémentez la logique de configuration spécifique à l'e-mail ici"
        )

    def envoyer_email(self, destinataire, sujet, contenu):
        """Envoyer un e-mail."""
        raise NotImplementedError("Implémentez la logique d'envoi d'e-mail ici")


class SMSNotificationStrategy(NotificationStrategy):
    """Stratégie de notification par SMS."""

    def envoyer(self, message):
        """Envoyer la notification par SMS."""
        print(f"Notification envoyée par SMS: {message}")

    def configurer(self, configuration):
        """Configurer la stratégie de SMS."""
        raise NotImplementedError(
            "Implémentez la logique de configuration spécifique au SMS ici"
        )

    def envoyer_sms(self, numero, message):
        """Envoyer un SMS."""
        raise NotImplementedError("Implémentez la logique d'envoi de SMS ici")


class PushNotificationStrategy(NotificationStrategy):
    """Stratégie de notification par push."""

    def envoyer(self, message):
        """Envoyer la notification par push."""
        print(f"Notification envoyée par push: {message}")

    def configurer(self, configuration):
        """Configurer la stratégie de push."""
        raise NotImplementedError(
            "Implémentez la logique de configuration spécifique au push ici"
        )

    def envoyer_push(self, destinataire, titre, contenu):
        """Envoyer une notification push."""
        raise NotImplementedError("Implémentez la logique d'envoi de push ici")

    def definir_priorite(self, priorite):
        """Définir la priorité de la notification push."""
        print(f"Priorité de la notification définie à: {priorite}")

    def verifier_etat(self):
        """Vérifier l'état de la notification push."""
        print("État de la notification push vérifié")


class NotificationContext:
    """Contexte de notification."""

    def __init__(self, strategy):
        """Initialiser le contexte avec une stratégie de notification."""
        self.strategy = strategy

    def notifier(self, message):
        """Notifier en utilisant la stratégie définie."""
        self.strategy.envoyer(message)
