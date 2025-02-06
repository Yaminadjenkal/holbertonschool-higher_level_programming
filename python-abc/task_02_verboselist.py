class verboselist(lis):
    def __init__(self, *args):
        super().__init__(*args)
    def append(self, item):
        print(f"Added [item] to the list.")
        super().append(item)
    def extend(self, item):
        print(f"Extended the list with [x] items.")
        super().extend(item)
        print(f"Extended the list with [x] items.")
        super().extend(item)
    def remove(self, item):
        print(f"Removed [item] from the list.")
        super().remove(item)
    def pop(self, item):
        print(f"Popped [item] from the list.")
        super().pop(item)
        
# Exemple d'utilisation
vlist = VerboseList([1, 2, 3])
vlist.append(4)
vlist.remove(2)
vlist.extend([5, 6])
print(vlist)