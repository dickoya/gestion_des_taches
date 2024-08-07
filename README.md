# gestion_des_taches

# Cahier des Charges : Gestionnaire de Tâches en Ligne de Commande

## Introduction
Ce cahier des charges décrit le développement d'un Gestionnaire de Tâches en Ligne de Commande. L'application permet à l'utilisateur de gérer une liste de tâches via une interface en ligne de commande. Les fonctionnalités incluent l'ajout, l'affichage, la modification, la suppression, la sauvegarde et le chargement des tâches.

## Objectifs
L'objectif principal est de fournir un outil simple et efficace pour gérer des tâches quotidiennes depuis une interface en ligne de commande.

## Fonctionnalités
Ajouter une tâche
    1. Description : Permet à l'utilisateur d'ajouter une nouvelle tâche.
    2. Entrée : Nom de la tâche.
    3. Sortie : Confirmation de l'ajout de la tâche.

## Afficher toutes les tâches
    1. Description : Affiche la liste de toutes les tâches avec leur statut.
    2. Entrée : Aucune.
    3. Sortie : Liste des tâches et leur statut (non terminée/terminée).

## Marquer une tâche comme terminée
    1.Description : Permet de marquer une tâche comme terminée.
    2.Entrée : Identifiant ou nom de la tâche.
    3.Sortie : Confirmation que la tâche a été marquée comme terminée.

## Supprimer une tâche
    1.Description : Permet de supprimer une tâche de la liste.
    2.Entrée : Identifiant ou nom de la tâche.
    3.Sortie : Confirmation de la suppression de la tâche.

## Sauvegarder les tâches dans un fichier
    Description : Sauvegarde la liste actuelle des tâches dans un fichier JSON.
    Entrée : Nom du fichier (facultatif).
    Sortie : Confirmation de la sauvegarde.
## Charger les tâches à partir d'un fichier
    Description : Charge les tâches à partir d'un fichier JSON existant.
    Entrée : Nom du fichier.
    Sortie : Confirmation du chargement et affichage des tâches chargées.

## Étapes de Développement
1. Structure de base du programme
Fichier principal : Créez un fichier main.py.
Boucle principale : Ajoutez une boucle principale pour afficher un menu et lire les entrées de l'utilisateur.
2. Ajouter une tâche
Fonction : Implémentez une fonction ajouter_tache.
Dictionnaire de tâche : Chaque tâche est représentée par un dictionnaire avec les clés "nom" et "statut" (ex. : {"nom": "Acheter du lait", "statut": "non terminée"}).
3. Afficher toutes les tâches
Fonction : Implémentez une fonction afficher_taches.
4. Marquer une tâche comme terminée
Fonction : Implémentez une fonction marquer_tache_terminee.
5. Supprimer une tâche
Fonction : Implémentez une fonction supprimer_tache.
6. Sauvegarder les tâches dans un fichier
Fonction : Utilisez le module json pour implémenter une fonction sauvegarder_taches.
7. Charger les tâches à partir d'un fichier
Fonction : Utilisez le module json pour implémenter une fonction charger_taches.

# Exigences Techniques
Langage de programmation : Python 3.x
Modules : json

## Conclusion
Ce cahier des charges définit les fonctionnalités et les étapes nécessaires pour développer un gestionnaire de tâches en ligne de commande. Le projet met en œuvre des fonctionnalités essentielles pour gérer efficacement des tâches et assurer leur persistance via des fichiers JSON.