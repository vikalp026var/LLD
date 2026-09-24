# Visitor: add new operations without changing the element classes.
# Each element only knows how to accept a visitor and dispatch to the right visit_* method.

from abc import ABC, abstractmethod
import math


# ----------- Element Interface -----------
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: "ShapeVisitor"):
        pass


# ----------- Concrete Elements -----------
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def accept(self, visitor: "ShapeVisitor"):
        return visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def accept(self, visitor: "ShapeVisitor"):
        return visitor.visit_rectangle(self)


# ----------- Visitor Interface -----------
class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: Circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: Rectangle):
        pass


# ----------- Concrete Visitors -----------
class AreaCalculator(ShapeVisitor):
    def visit_circle(self, circle: Circle):
        return math.pi * circle.radius ** 2

    def visit_rectangle(self, rectangle: Rectangle):
        return rectangle.width * rectangle.height


class PerimeterCalculator(ShapeVisitor):
    def visit_circle(self, circle: Circle):
        return 2 * math.pi * circle.radius

    def visit_rectangle(self, rectangle: Rectangle):
        return 2 * (rectangle.width + rectangle.height)


# ----------- Client Code -----------
def main():
    shapes = [Circle(5), Rectangle(3, 4)]
    area = AreaCalculator()
    perimeter = PerimeterCalculator()

    for shape in shapes:
        print(f"{type(shape).__name__} area: {shape.accept(area):.2f}")
        print(f"{type(shape).__name__} perimeter: {shape.accept(perimeter):.2f}")


if __name__ == "__main__":
    main()
