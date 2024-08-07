import json

# Liste des tâches
taches = []

def afficher_menu():
    print("\nMenu:")
    print("1. Ajouter une tâche")
    print("2. Afficher toutes les tâches")
    print("3. Marquer une tâche comme terminée")
    print("4. Supprimer une tâche")
    print("5. Sauvegarder les tâches")
    print("6. Charger les tâches")
    print("7. Quitter")



def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")
        if choix == '1':
            ajouter_tache()
        elif choix == '2':
            afficher_taches()
        elif choix == '3':
            marquer_tache()
        elif choix == '4':
            supprimer_tache()
        elif choix == '5':
            sauvegarder_taches()
        elif choix == '6':
            charger_taches()
        elif choix == '7':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
