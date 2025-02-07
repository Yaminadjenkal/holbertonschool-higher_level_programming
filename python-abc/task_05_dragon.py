# task_05_dragon.py

# Définition de la classe SwimMixin
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# Définition de la classe FlyMixin
class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Définition de la classe Dragon
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

# Exemple d'utilisation
if __name__ == "__main__":
    draco = Dragon()
    draco.swim()  # Outputs: The creature swims!
    draco.fly()   # Outputs: The creature flies!
    draco.roar()  # Outputs: The dragon roars!
