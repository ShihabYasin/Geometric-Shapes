###############################################################################
# IMPORTANT:
# THE CODE BELOW IS READ ONLY CODE AND YOU SHOULD INSPECT IT TO SEE WHAT IT
# DOES IN ORDER TO COMPLETE THE TASK, BUT DO NOT MODIFY IT IN ANY WAY AS THAT
# WILL RESULT IN A TEST FAILURE
###############################################################################

import abc


class ShapeInterface(metaclass=abc.ABCMeta):
    """
    Class that defines methods for all shapes
    """

    @abc.abstractmethod
    def get_perimeter(self) -> float:
        pass

    @abc.abstractmethod
    def get_area(self) -> float:
        pass
