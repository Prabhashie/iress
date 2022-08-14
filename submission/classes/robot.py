"""
file name:      robot.py
author:         Sachinthana Pathiranage
date created:   09/08/2022
purpose:        Class definition for the toy robot functionality
version:        1.0
"""
# imports
from classes.grid import Grid
from libs.log_msgs import *

class Robot:
    """Robot class containing the basic movements of the toy robot. 
    Once an object is created, it can be used to provide instructions to move the robot on the board.
    If xDim and yDim are not specified, default grid will be 5X5.
    """
    def __init__(self, grid: Grid) -> None:
        """Constructor method.
        """
        self.x = None
        self.y = None
        self.f = None
        self.grid = grid

    def validCoords(grid: Grid, x: int, y: int):
        if 0 <= x < grid.xDim and 0 <= y < grid.yDim:
            return True
        return False

    def place(self, x: int, y: int, f:str) -> None:
        """Places the robot in the grid location specified by x and y, facing the direction specified by f.

        :param x: Initial x position of the robot.
        :type x: int
        :param y: Initial y position of the robot.
        :type y: int
        :param f: Initial direction of facing of the robot.
        :type f: str
        :return: If placement is valid, log message.
        :rtype: bool, str or None
        """
        if self.validCoords(self.grid, x, y):
            self.x = x
            self.y = y
            self.f = f
            return True, None
        else:
            return False, INVALID_COORD_RANEG_ERR

    def move(self) -> None:
        """Move the robot.

        :return: If move is valid, log message.
        :rtype: bool, str or None
        """
        newX, newY = self.x, self.y # assume new coords are valid
        if self.f == "NORTH":
            newY = self.y + 1
        elif self.f == "SOUTH":
            newY = self.y - 1
        elif self.f == "EAST":
            newX = self.x + 1
        else:
            newX = self.x - 1
        
        if self.validCoords(self.grid, newX, newY): # validate coordinates within the board
            self.x = newX
            self.y = newY
            return True, None
        else:
            return False, INVALID_COORD_RANEG_ERR
    
    def turn(self, direction):
        """Turn the robot.

        :param direction: Turning direction.
        :type direction: str
        """
        if self.f == "NORTH":
            if direction == "LEFT":
                self.f = "WEST"
            else:
                self.f = "EAST"
        elif self.f == "SOUTH":
            if direction == "LEFT":
                self.f = "EAST"
            else:
                self.f = "WEST"
        elif self.f == "EAST":
            if direction == "LEFT":
                self.f = "NORTH"
            else:
                self.f = "SOUTH"
        else:
            if direction == "LEFT":
                self.f = "SOUTH"
            else:
                self.f = "NORTH"
    
    def report(self):
        """Output robot position details.

        :param x: x coordinate.
        :type x: int
        :param y: y coordinate.
        :type y: int
        :param f: Facing direction.
        :type f: str
        """
        print(f"Output: {self.x}, {self.y}, {self.f}")