###############################################################################
# WORKING AREA
# THIS IS AN AREA WHERE YOU SHOULD WRITE YOUR CODE AND MAKE CHANGES
###############################################################################
from typing import List
from geometric_shapes.exceptions.unsupported_shape_exception import UnsupportedShapeException
from geometric_shapes.geometric_shape import GeometricShape
from geometric_shapes.polygon_interface import PolygonInterface
from geometric_shapes.shape_interface import ShapeInterface


class Square (GeometricShape, ShapeInterface, PolygonInterface):

    def __init__(self, edges: List[float]):
        super ().__init__ ()
        self.name = self.__class__.__name__
        self.angle_count = 4
        self.edge = edges[0]

        if self.edge < 0:
            raise UnsupportedShapeException (shape_type="", supported_shapes="", message=f" With negative edge {self.name} is not Supported.")

    def get_name(self) -> str:
        return self.name

    def get_area(self) -> float:
        return round (self.edge * self.edge, 2)

    def get_perimeter(self) -> float:
        return round (4 * self.edge, 2)

    def get_angles(self) -> float:
        return self.angle_count
