#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Sérialiser un dictionnaire Python et l'enregistrer dans un fichier JSON.
    
    :param data: Un dictionnaire Python contenant les données
    :param filename: Le nom du fichier de sortie JSON. Si le fichier existe déjà, il sera remplacé.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Charger et désérialiser un fichier JSON pour recréer un dictionnaire Python.
    
    :param filename: Le nom du fichier JSON d'entrée
    :return: Un dictionnaire Python contenant les données désérialisées du fichier
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
    
