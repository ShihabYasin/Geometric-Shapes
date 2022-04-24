###############################################################################
# IMPORTANT:
# THE CODE BELOW IS READ ONLY CODE AND YOU SHOULD INSPECT IT TO SEE WHAT IT
# DOES IN ORDER TO COMPLETE THE TASK, BUT DO NOT MODIFY IT IN ANY WAY AS THAT
# WILL RESULT IN A TEST FAILURE
###############################################################################


class GeometricShape:
    """
    Base class for geometric objects
    """

    PI = 3.14

    def __init__(self):
        self.name = "GeometricShape"

    def get_name(self) -> str:
        return self.name
