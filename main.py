"""
Ce module contient la définition de la classe principale du projet.
"""

from projet import Projet, Tache, Membre, Jalon, Risque, Changement
from notification import NotificationContext, EmailNotificationStrategy

# Initialiser les stratégies de notification
notification_context = NotificationContext(EmailNotificationStrategy())

# Créer un projet
projet = Projet("Nouveau Produit", "Développement d'un nouveau produit",
                "2024-01-01", "2024-12-31", 100000)

# Ajouter des membres
membre1 = Membre("Modou", "Chef de projet")
membre2 = Membre("Christian", "Développeur")

projet.ajouter_membre_equipe(membre1)
notification_context.notifier(f"Notification envoyée à"
                              f" {membre1.nom} par email: {membre1.nom}"
                              f" a été ajouté à l'équipe")

projet.ajouter_membre_equipe(membre2)
notification_context.notifier(f"Notification envoyée à "
                              f"{membre2.nom} par email: {membre2.nom}"
                              f" a été ajouté à l'équipe")

# Ajouter des tâches
tache1 = Tache("Analyse des besoins",
               "Analyser les besoins des utilisateurs",
               "2024-01-01", "2024-01-31", membre1, "Terminée")
projet.ajouter_tache(tache1)
notification_context.notifier(f"Notification envoyée à "
                              f"{membre1.nom} par email: "
                              f"Nouvelle tâche ajoutée: {tache1.nom}")
notification_context.notifier(f"Notification envoyée à "
                              f"{membre2.nom} par email:"
                              f" Nouvelle tâche ajoutée: {tache1.nom}")

tache2 = Tache("Développement", "Développer le produit",
               "2024-02-01", "2024-06-30", membre2, "Non démarrée")
projet.ajouter_tache(tache2)
notification_context.notifier(f"Notification envoyée "
                              f"à {membre1.nom} par email:"
                              f" Nouvelle tâche ajoutée: {tache2.nom}")
notification_context.notifier(f"Notification envoyée à {membre2.nom}"
                              f" par email: Nouvelle tâche ajoutée:"
                              f" {tache2.nom}")

# Mettre à jour le budget
projet.budget = 50000
notification_context.notifier(f"Notification envoyée à"
                              f" {membre1.nom} par email: "
                              f"Le budget du projet a été défini à"
                              f" {projet.budget} Unité Monétaire")
notification_context.notifier(f"Notification envoyée à "
                              f"{membre2.nom} par email:"
                              f" Le budget du projet a été défini à"
                              f" {projet.budget} Unité Monétaire")

# Ajouter un risque
risque1 = Risque("Retard de livraison", 0.8, "Élevé")
projet.ajouter_risque(risque1)
notification_context.notifier(f"Notification envoyée à "
                              f"{membre1.nom} par email: "
                              f"Nouveau risque ajouté: {risque1.description}")
notification_context.notifier(f"Notification envoyée à "
                              f"{membre2.nom} par email: "
                              f"Nouveau risque ajouté: {risque1.description}")

# Ajouter un jalon
jalon1 = Jalon("Phase 1 terminée", "2024-01-31")
projet.ajouter_jalon(jalon1)
notification_context.notifier(f"Notification envoyée à "
                              f"{membre1.nom} par email: "
                              f"Nouveau jalon ajouté: {jalon1.nom}")
notification_context.notifier(f"Notification envoyée à "
                              f"{membre2.nom} par email: "
                              f"Nouveau jalon ajouté: {jalon1.nom}")

# Enregistrer un changement
changement1 = Changement("Changement de la portée du projet",
                         "1.1", "2024-02-15")
projet.enregistrer_changement(changement1)
notification_context.notifier(f"Notification envoyée à"
                              f" {membre1.nom} par email: "
                              f"Changement enregistré:"
                              f" {changement1.description} "
                              f"(version {changement1.version})")
notification_context.notifier(f"Notification envoyée à "
                              f"{membre2.nom} par email: "
                              f"Changement enregistré: "
                              f"{changement1.description} "
                              f"(version {changement1.version})")

# Générer le rapport d'activités
rapport = f"""
Rapport d'activités du Projet '{projet.nom}' Version: {changement1.version}
Dates: {projet.date_debut} à {projet.date_fin}
Budget: {projet.budget} Unité Monétaire
Equipe:
"""
for membre in projet.equipe.membres:
    rapport += f"⦁ {membre.nom} ({membre.role})\n"

rapport += "Tâches:\n"
for tache in projet.taches:
    rapport += f"⦁ {tache.nom} ({tache.date_debut} " \
               f"à {tache.date_fin}), Responsable: {tache.responsable.nom}, " \
               f"Statut: {tache.statut}\n"

rapport += "Jalons:\n"
for jalon in projet.jalons:
    rapport += f"⦁ {jalon.nom} ({jalon.date})\n"

rapport += "Risques:\n"
for risque in projet.risques:
    rapport += f"⦁ {risque.description} (Probabilité:" \
               f" {risque.probabilite}, Impact: {risque.impact})\n"

# Chemin Critique
rapport += "Chemin Critique:\n"
rapport += f"⦁ {tache1.nom} ({tache1.date_debut} à {tache1.date_fin})\n"
rapport += f"⦁ {tache2.nom} ({tache2.date_debut} à {tache2.date_fin})\n"

print(rapport)
