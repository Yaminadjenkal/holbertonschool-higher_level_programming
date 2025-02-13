import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        # Ouvrir le fichier CSV en mode lecture
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            # Utiliser DictReader pour lire les lignes du fichier CSV et les convertir en dictionnaires
            reader = csv.DictReader(csv_file)
            data_list = list(reader)
        
        # Ouvrir le fichier JSON en mode écriture
        with open('data.json', 'w', encoding='utf-8') as json_file:
            # Sérialiser la liste de dictionnaires en JSON et l'écrire dans le fichier
            json.dump(data_list, json_file, ensure_ascii=False, indent=4)
        
        return True
    except FileNotFoundError:
        # Gérer l'exception si le fichier CSV n'existe pas
        print(f"Erreur : le fichier {csv_filename} n'a pas été trouvé.")
        return False
    except Exception as e:
        # Gérer toutes les autres exceptions possibles
        print(f"Erreur : {e}")
        return False

# Exemple d'utilisation :
if __name__ == "__main__":
    # Remplacez 'votre_fichier.csv' par le nom du fichier CSV que vous souhaitez convertir
    resultat = convert_csv_to_json('votre_fichier.csv')
    if resultat:
        print("Conversion réussie !")
    else:
        print("Échec de la conversion.")
