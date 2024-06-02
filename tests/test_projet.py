"""Classe de test."""

import unittest
from projet import Projet, Tache, Membre, Risque, Jalon, Changement


class TestProjet(unittest.TestCase):
    """Classe de test pour la classe Projet."""

    def setUp(self):
        """Initialise les objets nécessaires aux tests."""
        self.projet = Projet(
            "Nouveau Projet", "Description", "2024-01-01", "2024-12-31", 10000
        )
        self.tache = Tache(
            "Tâche 1",
            "Description",
            "2024-01-01",
            "2024-01-31",
            "Responsable",
            "Non commencée",
        )
        self.membre = Membre("John Doe", "Développeur")
        self.risque = Risque("Risque 1", "Élevé", "Probable")
        self.jalon = Jalon("Jalon 1", "2024-06-30")
        self.changement = Changement("Changement1", "version1", "2024-03-15")

    def test_ajouter_tache(self):
        """Teste la méthode ajouter_tache de la classe Projet."""
        projet = Projet(
            "Nouveau Projet", "Description", "2024-01-01", "2024-12-31", 10000
        )
        tache = Tache(
            "Tâche 1",
            "Description",
            "2024-01-01",
            "2024-01-31",
            "Responsable",
            "Non commencée",
        )
        projet.ajouter_tache(tache)
        self.assertEqual(len(projet.taches), 1)
        self.assertEqual(projet.taches[0].nom, "Tâche 1")

    def test_ajouter_membre_equipe(self):
        """Teste la méthode ajouter_membre_equipe de la classe Projet."""
        self.projet.ajouter_membre_equipe(self.membre)
        self.assertEqual(len(self.projet.equipe.membres), 1)
        self.assertEqual(self.projet.equipe.membres[0].nom, "John Doe")

    def test_ajouter_risque(self):
        """Teste la méthode ajouter_risque de la classe Projet."""
        self.projet.ajouter_risque(self.risque)
        self.assertEqual(len(self.projet.risques), 1)
        self.assertEqual(self.projet.risques[0].description, "Risque 1")

    def test_ajouter_jalon(self):
        """Teste la méthode ajouter_jalon de la classe Projet."""
        self.projet.ajouter_jalon(self.jalon)
        self.assertEqual(len(self.projet.jalons), 1)
        self.assertEqual(self.projet.jalons[0].nom, "Jalon 1")

    def test_enregistrer_changement(self):
        """Teste la méthode enregistrer_changement de la classe Projet."""
        self.projet.enregistrer_changement(self.changement)
        self.assertEqual(len(self.projet.changements), 1)
        self.assertEqual(self.projet.changements[0].description, "Changement1")


if __name__ == "__main__":
    unittest.main()
