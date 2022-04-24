###############################################################################
# WORKING AREA
# THIS IS AN AREA WHERE YOU SHOULD WRITE YOUR CODE AND MAKE CHANGES
###############################################################################
class UnsupportedShapeException (Exception):

    def __init__(self, shape_type, supported_shapes, message=" is not a supported shape type. Please choose shape type from: "):
        self.shape_type = shape_type
        self.message = message
        self.supported_shapes = supported_shapes
        super ().__init__ (self.message)

    def __str__(self):
        return f'{self.shape_type} {self.message} {self.supported_shapes}'
