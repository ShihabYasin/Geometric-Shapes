###############################################################################
# WORKING AREA
# THIS IS AN AREA WHERE YOU SHOULD WRITE YOUR CODE AND MAKE CHANGES
###############################################################################
from typing import List
from geometric_shapes.circle import Circle
from geometric_shapes.exceptions.unsupported_shape_exception import UnsupportedShapeException
from geometric_shapes.exceptions.wrong_param_count_exception import WrongParamCountException
from geometric_shapes.rectangle import Rectangle
from geometric_shapes.square import Square


class ShapeFactory:
    SUPPORTED_SHAPES = ['Circle', 'Square', 'Rectangle']
    VALID_PARAMS = [1, 1, 2]

    @staticmethod
    def create_shape(shape: str, params: List[float]):
        """
        Creates a specific GeometricShape object from the given attributes.

        Usage examples:
            ShapeFactory.create_shape("Circle", 4)
            ShapeFactory.create_shape("Rectangle", [3, 5])

        Parameters:
            shape: str Shape to create.
            params: List[float] List of required parameters.
        """

        if shape not in ShapeFactory.SUPPORTED_SHAPES:
            raise UnsupportedShapeException (shape_type=shape, supported_shapes=ShapeFactory.SUPPORTED_SHAPES)

        expected_param_count = ShapeFactory.VALID_PARAMS[ShapeFactory.SUPPORTED_SHAPES.index (shape)]

        if params is None:
            raise WrongParamCountException (shape_type=shape, message=f"Expected 'params' Count {expected_param_count} not None for ")

        passed_params_len = len (params)

        if passed_params_len != expected_param_count:
            raise WrongParamCountException (shape_type=shape, message=f"Expected 'params' Count {expected_param_count}, found {passed_params_len} ; 'params' count not valid for ")

        geometric_shape_obj = {
            "Circle": Circle,
            "Square": Square,
            "Rectangle": Rectangle,
            }

        return geometric_shape_obj[shape] (params)
