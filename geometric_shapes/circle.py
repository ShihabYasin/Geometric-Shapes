###############################################################################
# WORKING AREA
# THIS IS AN AREA WHERE YOU SHOULD WRITE YOUR CODE AND MAKE CHANGES
###############################################################################
from typing import List
from geometric_shapes.exceptions.unsupported_shape_exception import UnsupportedShapeException
from geometric_shapes.geometric_shape import GeometricShape
from geometric_shapes.shape_interface import ShapeInterface


class Circle (GeometricShape, ShapeInterface):
    PI = GeometricShape.PI

    def __init__(self, radius: List[float]):
        super ().__init__ ()
        self.name = self.__class__.__name__
        self.radius = radius[0]

        if self.radius < 0:
            raise UnsupportedShapeException (shape_type="", supported_shapes="", message=f" With negative radius {self.radius} {self.name} is not Supported.")

    def get_name(self) -> str:
        return self.name

    def get_area(self) -> float:
        return round (Circle.PI * (self.radius ** 2), 2)

    def get_perimeter(self) -> float:
        return round (2 * Circle.PI * self.radius, 2)
