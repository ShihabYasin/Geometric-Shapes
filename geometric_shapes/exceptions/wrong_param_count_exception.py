###############################################################################
# WORKING AREA
# THIS IS AN AREA WHERE YOU SHOULD WRITE YOUR CODE AND MAKE CHANGES
###############################################################################

class WrongParamCountException (Exception):

    def __init__(self, shape_type, message="Parameters count not valid for "):
        self.shape_type = shape_type
        self.message = message
        super ().__init__ (self.message)

    def __str__(self):
        return f' {self.message} {self.shape_type}'
