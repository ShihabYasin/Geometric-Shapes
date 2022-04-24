###############################################################################
# WORKING AREA
# THIS IS AN AREA WHERE YOU SHOULD WRITE YOUR CODE AND MAKE CHANGES
###############################################################################
from typing import List
from geometric_shapes.exceptions.unsupported_shape_exception import UnsupportedShapeException
from geometric_shapes.geometric_shape import GeometricShape
from geometric_shapes.polygon_interface import PolygonInterface
from geometric_shapes.shape_interface import ShapeInterface


class Rectangle (GeometricShape, ShapeInterface, PolygonInterface):

    def __init__(self, edges: List[float]):
        super ().__init__ ()
        self.name = self.__class__.__name__
        self.angle_count = 4
        self.first_edge, self.second_edge = edges[0], edges[1]

        if self.first_edge < 0 or self.second_edge < 0:
            raise UnsupportedShapeException (shape_type="", supported_shapes="", message=f" With negative edge {self.name} is not Supported.")

    def get_name(self) -> str:
        return self.name

    def get_area(self) -> float:
        return round (self.first_edge * self.second_edge, 2)

    def get_perimeter(self) -> float:
        return round (2 * (self.first_edge + self.second_edge), 2)

    def get_angles(self) -> float:
        return self.angle_count
