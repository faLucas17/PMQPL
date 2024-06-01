import unittest
from projet import Projet, Tache, Membre

class TestProjet(unittest.TestCase):
    def test_ajouter_tache(self):
        projet = Projet("Nouveau Projet", "Description", "2024-01-01", "2024-12-31", 10000)
        tache = Tache("Tâche 1", "Description", "2024-01-01", "2024-01-31", "Responsable", "Non commencée")
        projet.ajouter_tache(tache)
        self.assertEqual(len(projet.taches), 1)
        self.assertEqual(projet.taches[0].nom, "Tâche 1")

if __name__ == '__main__':
    unittest.main()
