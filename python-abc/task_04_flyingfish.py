# task_04_flyingfish.py

# Définition de la classe Fish
class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

# Définition de la classe Bird
class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

# Définition de la classe FlyingFish
class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

# Exemple d'utilisation
if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()

    # Affiche l'ordre de résolution des méthodes (MRO)
    print(FlyingFish.mro())
