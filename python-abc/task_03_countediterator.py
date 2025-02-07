# task_03_countediterator.py

# Définition de la classe CountedIterator
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)  # Crée un itérateur à partir de l'itérable
        self.count = 0  # Initialise le compteur à 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)  # Obtient le prochain élément de l'itérateur
            self.count += 1  # Incrémente le compteur
            return item  # Retourne l'élément
        except StopIteration:
            # Si l'itérateur est épuisé, lève l'exception StopIteration
            raise StopIteration

    def get_count(self):
        return self.count  # Retourne la valeur actuelle du compteur

# Exemple d'utilisation
if __name__ == "__main__":
    data = [1, 2, 3, 4]  # Liste d'éléments
    counted_iter = CountedIterator(data)  # Crée une instance de CountedIterator

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
    except StopIteration:
        print("No more items.")

