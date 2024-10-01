from abc import ABC, abstractmethod

# Abstract base class for all polygons
class Polygon(ABC):
    
    @abstractmethod
    def area(self):
        pass

# Class for rectangle
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Class for square (a special case of a rectangle)
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

# Class for triangle
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Example usage:
if __name__ == "__main__":
    rect = Rectangle(5, 3)
    print(f"Area of rectangle: {rect.area()}")

    square = Square(4)
    print(f"Area of square: {square.area()}")

    tri = Triangle(6, 7)
    print(f"Area of triangle: {tri.area()}")
