"""
file name:      robot.py
author:         Sachinthana Pathiranage
date created:   09/08/2022
purpose:        Class definition for the toy robot functionality
version:        1.0
"""
# imports

class Robot:
    """Robot class containing the basic movements of the toy robot. 
    Once an object is created, it can be used to provide instructions to move the robot in the grid specified by xDim and yDim.
    If xDim and yDim are not specified, default grid will be 5X5.

    :param xDim: Grid size - x dimension
    :type xDim: int, optional
    :param yDim: Grid size - y dimension
    :type yDim: int, optional
    """
    def __init__(self, xDim = 5, yDim = 5) -> None:
        """Constructor method
        """
        self.xDim = xDim
        self.yDim = yDim
        self.x = None
        self.y = None
        self.f = None

    def place(self, x, y, f) -> None:
        """Places the robot in the grid location specified by x and y facing the direction specified by f.

        :param x: Initial x position of the robot
        :type x: int
        :param y: Initial y position of the robot
        :type y: int
        :param f: Initial direction of facing of the robot
        :type f: str
        """
        self.x = x
        self.y = y
        self.f = f

