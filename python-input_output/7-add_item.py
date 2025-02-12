#!/usr/bin/python3
"""Script to add all arguments to a Python list and save to a file"""

import sys

# Importation des fonctions des autres fichiers
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    # Tente de charger la liste existante depuis le fichier
    arglist = load_from_json_file("add_item.json")
except FileNotFoundError:
    # Si le fichier n'existe pas, initialise une nouvelle liste vide
    arglist = []

# Ajoute les arguments de la ligne de commande à la liste
arglist.extend(sys.argv[1:])

# Sauvegarde la liste mise à jour dans le fichier JSON
save_to_json_file(arglist, "add_item.json")

