"""Module de gestion des projets."""

from collections import namedtuple

Membre = namedtuple("Membre", ["nom", "role"])
Tache = namedtuple("Tache", ["nom", "description",
                             "date_debut", "date_fin",
                             "responsable", "statut"])
Jalon = namedtuple("Jalon", ["nom", "date"])
Risque = namedtuple("Risque", ["description", "probabilite", "impact"])
Changement = namedtuple("Changement", ["description", "version", "date"])


class Equipe:
    """Représente une équipe de projet."""

    def __init__(self):
        self.membres = []

    def ajouter_membre(self, membre):
        """Ajoute un membre à l'équipe."""
        self.membres.append(membre)


class Projet:
    """Représente un projet."""

    def __init__(self, nom, description, date_debut, date_fin, budget):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.budget = budget
        self.taches = []
        self.equipe = Equipe()
        self.risques = []
        self.jalons = []
        self.changements = []

    def ajouter_tache(self, tache):
        """Ajoute une tâche au projet."""
        self.taches.append(tache)

    def ajouter_membre_equipe(self, membre):
        """Ajoute un membre à l'équipe du projet."""
        self.equipe.ajouter_membre(membre)

    def ajouter_risque(self, risque):
        """Ajoute un risque au projet."""
        self.risques.append(risque)

    def ajouter_jalon(self, jalon):
        """Ajoute un jalon au projet."""
        self.jalons.append(jalon)

    def enregistrer_changement(self, changement):
        """Enregistre un changement dans le projet."""
        self.changements.append(changement)
