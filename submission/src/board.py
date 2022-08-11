"""
file name:      board.py
author:         Sachinthana Pathiranage
date created:   11/08/2022
purpose:        Class definition for the board the robot traverses
version:        1.0
"""
# imports

class Board:
    """Board class on which the board moves. 
    Once an object is created, it can be used specify the dimensions of the board the robot moves.
    If xDim and yDim are not specified, default grid will be 5X5.

    :param xDim: Grid size - x dimension
    :type xDim: int, optional
    :param yDim: Grid size - y dimension
    :type yDim: int, optional
    """
    def __init__(self, xDim = 5, yDim = 5) -> None:
        """Constructor method.
        """
        self.xDim = xDim
        self.yDim = yDim