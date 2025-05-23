from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

# Concrete class
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Usage
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print("Area of rectangle:", rect.area())
