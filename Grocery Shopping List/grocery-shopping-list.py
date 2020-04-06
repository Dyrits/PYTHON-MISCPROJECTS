import os
import json

folder_path = os.path.dirname(__file__)
json_path = os.path.join(folder_path, "liste.json")

if os.path.exists(json_path):
    with open(json_path, "r") as json_list:
        grocery_shopping_list = json.load(json_list)
else:
    grocery_shopping_list = []

options = ["Ajouter un élément", "Enlever un élément",
           "Afficher la liste", "Vider la liste", "Terminer"]


# Fonction affichant les options du menu principal :
def user_options():
    print("Que voulez-vous faire ?")
    for index, option in enumerate(options):
        print(f"{index + 1}/ {option}")


# Fonction permettant d'ajouter un élément à la liste de course :
def add_element():
    print()
    element = input(("Que voulez-vous ajouter ? "))
    grocery_shopping_list.append(element)


# Fonction permettant d'afficher la liste de course :
def display_list():
    print()
    if not grocery_shopping_list:
        print("La liste est vide !")
    else:
        print("Voici la liste de course: ")
        for element in grocery_shopping_list:
            print(f"- {element}")


# Fonction permettant de retirer un élément de la liste de course :
def remove_element():
    display_list()
    print()
    try:
        grocery_shopping_list.remove(
            input("Quel élément souhaitez-vous enlever ? "))
    except:
        print("Cet élément ne fait pas partie de la liste !")


# Fonction permettant de vider totalement la liste de course :
def empty_list():
    print()
    if not grocery_shopping_list:
        print("La liste est déjà vide !")
    else:
        empty_list = None
        while empty_list == None:
            empty_list = input(
                "Voulez-vous vraiment vider la liste ? O/N : ").lower()
            if empty_list == "o":
                grocery_shopping_list.clear()
                print("La liste a été vidée !")
            elif empty_list == "n":
                pass
            else:
                print("Veuillez saisir O pour Oui ou N pour N")
                empty_list = None
    
    
# Fonction permettant de sauvegarder la liste et quitter le programme:              
def terminate():
    with open(json_path, "w") as json_list:
        json.dump(grocery_shopping_list, json_list, indent=4)
    exit()


# Fonction permettant de lancer la fonction correspondante au choix de l'utilisateur :
def option_output(user_choice):
    if user_choice == 1:
        add_element()
    if user_choice == 2:
        remove_element()
    if user_choice == 3:
        display_list()
    if user_choice == 4:
        empty_list()
    if user_choice == 5:
        terminate()


# Fonction déterminant le choix de l'utilisateur :
def user_choice():
    user_options()
    user_choice = None
    while user_choice == None:
        try:
            user_choice = int(input("Choisissez une option: "))
            if len(options) < user_choice or user_choice < 1:
                user_choice = None
                print("Option invalide !")
        except:
            print("Veuillez saisir un nombre !")
            user_choice = None
    return user_choice


# Boucle principale du programme :
while True:
    option_output(user_choice())
    print()