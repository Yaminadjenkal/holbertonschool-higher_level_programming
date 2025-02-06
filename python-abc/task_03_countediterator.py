#!/usr/bin/python3

# Définition de la classe CountedIterator
class CountedIterator:
    # Initialisation de l'itérateur avec l'itérable donné
    def __init__(self, iterable):
        self.iterable = iterable  # Enregistre l'itérable
        self.iterator = iter(iterable)  # Crée un itérateur à partir de l'itérable
        self.count = 0  # Initialise le compteur à 0

    # Méthode spéciale pour retourner l'itérateur lui-même
    def __iter__(self):
        return self

    # Méthode spéciale pour obtenir l'élément suivant de l'itérateur
    def __next__(self):
        try:
            # Obtient le prochain élément de l'itérateur
            item = next(self.iterator)
            self.count += 1  # Incrémente le compteur
            print(f"Iteration {self.count}: {item}")  # Affiche le compteur et l'élément
            return item  # Retourne l'élément
        except StopIteration:
            # Si l'itérateur est épuisé, lève l'exception StopIteration
            raise StopIteration

# Exemple d'utilisation
if __name__ == "__main__":
    items = [1, 2, 3, 4, 5]  # Liste d'éléments
    counted_iter = CountedIterator(items)  # Crée une instance de CountedIterator

    # Itère sur les éléments de counted_iter
    for item in counted_iter:
        pass  # Pass signifie qu'on ne fait rien de spécial avec les éléments dans cet exemple
