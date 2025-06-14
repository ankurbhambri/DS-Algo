'''
    Imagine filling out a resume. Instead of starting from scratch every time, we can copy an existing resume template and just change a few details — that is a prototype.
'''

from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Circle(Prototype):
    def __init__(self, radius: float, color: str):
        self.radius = radius
        self.color = color

    def clone(self):
        # Deep copy ensures no shared references
        return copy.deepcopy(self)

    def __str__(self):
        return f"Circle(radius={self.radius}, color='{self.color}')"

class Rectangle(Prototype):
    def __init__(self, width: float, height: float, color: str):
        self.width = width
        self.height = height
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, color='{self.color}')"


if __name__ == "__main__":

    # Original objects
    circle1 = Circle(radius=10, color="red")
    rect1 = Rectangle(width=5, height=10, color="blue")

    # Cloning the objects
    circle2 = circle1.clone()
    rect2 = rect1.clone()

    # Modify cloned instance
    circle2.color = "green"
    rect2.height = 20

    # Print to verify
    print("Original:", circle1)
    print("Clone   :", circle2)

    print("Original:", rect1)
    print("Clone   :", rect2)
