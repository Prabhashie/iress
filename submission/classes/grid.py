"""
file name:      grid.py
author:         Sachinthana Pathiranage
date created:   11/08/2022
purpose:        Class definition for the grid, the robot traverses
version:        1.0
"""
# imports

class Grid:
    """Grid class on which the robot moves. 
    Once an object is created, it can be used specify the dimensions of the grid, the robot moves.
    If xDim and yDim are not specified, default grid will be 5X5.

    :param xDim: Grid size - x dimension
    :type xDim: int, optional
    :param yDim: Grid size - y dimension
    :type yDim: int, optional
    """
    def __init__(self, xDim = 5, yDim = 5):
        """Constructor method.
        """
        self.xDim = xDim
        self.yDim = yDim
    
    def change_dims(self, newX, newY):
        """Change grid dimensions.

        :param newX: New x dimension.
        :type newX: int
        :param newY: New y dimension.
        :type newY: int
        """
        self.xDim = newX
        self.yDim = newY