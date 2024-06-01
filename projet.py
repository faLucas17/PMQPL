# projet.py

class Membre:
    def __init__(self, nom, role):
        self.nom = nom
        self.role = role

class Equipe:
    def __init__(self):
        self.membres = []

    def ajouter_membre(self, membre):
        self.membres.append(membre)

class Tache:
    def __init__(self, nom, description, date_debut, date_fin, responsable, statut):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.responsable = responsable
        self.statut = statut

class Jalon:
    def __init__(self, nom, date):
        self.nom = nom
        self.date = date

class Risque:
    def __init__(self, description, probabilite, impact):
        self.description = description
        self.probabilite = probabilite
        self.impact = impact

class Changement:
    def __init__(self, description, version, date):
        self.description = description
        self.version = version
        self.date = date

class Projet:
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
        self.taches.append(tache)

    def ajouter_membre_equipe(self, membre):
        self.equipe.ajouter_membre(membre)

    def ajouter_risque(self, risque):
        self.risques.append(risque)

    def ajouter_jalon(self, jalon):
        self.jalons.append(jalon)

    def enregistrer_changement(self, changement):
        self.changements.append(changement)
