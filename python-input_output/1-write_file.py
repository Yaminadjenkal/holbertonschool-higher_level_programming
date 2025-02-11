#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Écrit une chaîne de caractères dans un fichier texte (UTF8) et renvoie le nombre de caractères écrits.

    :param filename: Nom du fichier
    :param text: Texte à écrire dans le fichier
    :return: Nombre de caractères écrits
    """
    # Utilisation de l'instruction 'with' pour ouvrir le fichier en mode écriture
    with open(filename, "w", encoding="utf-8") as f:
        # Écrire le texte dans le fichier et retourner le nombre de caractères écrits
        return f.write(text)

# Exemple d'utilisation de la fonction
if __name__ == "__main__":
    # Appel de la fonction write_file avec un nom de fichier et un texte
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    # Affichage du nombre de caractères écrits
    print(nb_characters)
