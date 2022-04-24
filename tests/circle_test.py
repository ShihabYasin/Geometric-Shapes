###############################################################################
# TESTING AREA
# THIS IS AN AREA WHERE YOU CAN TEST YOUR WORK AND WRITE YOUR OWN UNIT TESTS
###############################################################################
import unittest
from geometric_shapes.circle import Circle
from geometric_shapes.exceptions.unsupported_shape_exception import (
    UnsupportedShapeException
    )
from geometric_shapes.exceptions.wrong_param_count_exception import (
    WrongParamCountException,
    )
from geometric_shapes.geometric_shape import GeometricShape
from geometric_shapes.polygon_interface import PolygonInterface
from geometric_shapes.shape_factory import ShapeFactory
from geometric_shapes.shape_interface import ShapeInterface


class CircleTest (unittest.TestCase):

    def setUp(self):
        self.circle = ShapeFactory.create_shape ("Circle", [34.445])

    def test_create_circle_object(self):
        self.assertIsInstance (self.circle, Circle)

    def test_circle_object_has_correct_name(self):
        self.assertEqual (self.circle.get_name (), "Circle")

    def test_returns_correct_area(self):
        self.assertEqual (self.circle.get_area (), 3725.48)

    def test_returns_correct_perimeter(self):
        self.assertEqual (self.circle.get_perimeter (), 216.31)

    def test_implements_geometric_shape(self):
        self.assertIsInstance (self.circle, GeometricShape)

    def test_implements_shape_interface(self):
        self.assertIsInstance (self.circle, ShapeInterface)

    def test_does_not_implement_polygon_interface(self):
        self.assertNotIsInstance (self.circle, PolygonInterface)

    def test_should_throw_wrong_param_count_exception(self):
        with self.assertRaises (WrongParamCountException):
            ShapeFactory.create_shape ("Circle", [])

    def test_should_throw_wrong_param_count_exception_2(self):
        with self.assertRaises (WrongParamCountException):
            ShapeFactory.create_shape ("Circle", [1, 4])

    def test_should_throw_wrong_param_count_exception_3(self):
        with self.assertRaises (WrongParamCountException):
            ShapeFactory.create_shape ("Circle", [7, -8])

    def test_should_throw_wrong_param_count_exception_4(self):
        with self.assertRaises (WrongParamCountException):
            self.circle = ShapeFactory.create_shape ('Circle', None)

    def test_does_not_implement_negative_radius_area(self):
        with self.assertRaises (UnsupportedShapeException):
            ShapeFactory.create_shape ("Circle", [-1])

    def test_should_throw_unsupported_shape_exception(self):
        with self.assertRaises (UnsupportedShapeException):
            self.circle = ShapeFactory.create_shape ("otestCircle", [4])

    def test_should_throw_unsupported_shape_exception_2(self):
        with self.assertRaises (UnsupportedShapeException):
            self.circle = ShapeFactory.create_shape ("", [4])

    def test_should_throw_unsupported_shape_exception_3(self):
        with self.assertRaises (UnsupportedShapeException):
            self.circle = ShapeFactory.create_shape ([2], 'Circle')


if __name__ == "__main__":
    unittest.main ()
