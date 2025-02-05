from abc import ABC, abstractmethod

# Créer le modèle général pour les formes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Créer une sous-classe pour les cercles
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Créer une sous-classe pour les rectangles
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
