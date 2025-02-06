#!/usr/bin/python3
class VerboseList(list):
    def __init__(self, *args):
        super().__init__(*args)

    def append(self, item):
        print(f"Ajout de {item} à la liste.")
        super().append(item)

    def extend(self, items):
        print(f"Extension de la liste avec {len(items)} éléments.")
        super().extend(items)

    def remove(self, item):
        print(f"Suppression de {item} de la liste.")
        super().remove(item)

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Élément {item} supprimé de la liste à l'index {index}.")
        return item

        