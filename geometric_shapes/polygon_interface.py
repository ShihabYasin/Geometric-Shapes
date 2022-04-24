###############################################################################
# IMPORTANT:
# THE CODE BELOW IS READ ONLY CODE AND YOU SHOULD INSPECT IT TO SEE WHAT IT
# DOES IN ORDER TO COMPLETE THE TASK, BUT DO NOT MODIFY IT IN ANY WAY AS THAT
# WILL RESULT IN A TEST FAILURE
###############################################################################

import abc


class PolygonInterface(metaclass=abc.ABCMeta):
    """
    Class that defines methods for polygon shapes
    """

    @abc.abstractmethod
    def get_angles(self) -> int:
        pass
