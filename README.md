### Notes:

1. get_angles()  function was not very clearly mentioned i.e: if it is count of inner angles or number of angles in a polygon (for square & rectangle number of angles is 4, so used it for implementation).
2. It is assumed that negative radius and edge length for polygon are invalid.

# Geometric Shapes

## Description

As part of a bigger project you are required to implement a basic data model that will represent geometric shapes.

Team lead in charge of this project has defined interfaces and base classes that should be used and prepared a simple test code that will help you test your work.

Your job is to finish this implementation by adding support for circle, square and rectangle shapes.

## Technical Requirements

You need to add classes to support required shapes.
Supported shapes are defined as:
* `Circle` is defined by a single parameter representing radius.
* `Square` is also defined by a single parameter representing edge size.
* `Rectangle` is defined by two parameters representing size of each edge.

Use defined constant `PI` from `GeometricShape` class for calculating area and perimeter of circle.

You need to finish implementing factory class called `ShapeFactory` that will be used to create specific `GeometricShape` instances.

You need to define and throw proper exceptions based on test code provided by team lead.



## Automatic Testing

Team lead will use their test suite to run automatic tests to verify your implementation.

So you need to follow the instructions in source code comments in order to make sure that your code will work correctly with automatic tests.

You should define your classes in files `circle.py`, `rectangle.py`, `square.py`, `unsupported_shape_exception.py`, `wrong_param_count_exception.py` and finish the implementation of `ShapeFactory` class in module `shape_factory.py`.

Files `geometric_shape.py`, `polygon_interface.py`, `shape_interface.py` should not be altered in any way. You should only inspect them to understand better what needs to be done.

Files under `tests` directory provide two example test cases taken from team lead's test suite. You should read them to figure out how to properly implement shape classes and throw exceptions.

You are also encouraged to write your own test cases under `tests` directory.
