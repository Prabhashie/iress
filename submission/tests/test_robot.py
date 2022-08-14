"""
file name:      test_robot.py
author:         Sachinthana Pathiranage
date created:   14/08/2022
purpose:        Unit tests for Robot class
version:        1.0
"""

# imports
import unittest
from io import StringIO 
import sys
from classes.robot import Robot
from classes.grid import Grid
from libs.log_msgs import *

class TestGrid(unittest.TestCase):
    def test_init(self): # test init function
        grid = Grid()
        robot = Robot(grid)
        self.assertEqual(robot.x, None)
        self.assertEqual(robot.y, None)
        self.assertEqual(robot.f, None)
        self.assertIsInstance(robot.grid, Grid)
    
    def test_validCoords(self): # test validCoords function
        grid = Grid()
        robot = Robot(grid)
        self.assertTrue(robot.validCoords(3, 4))
        self.assertFalse(robot.validCoords(6, 7))
        self.assertFalse(robot.validCoords(4, 5))
        self.assertFalse(robot.validCoords(5, 4))
        self.assertFalse(robot.validCoords(5, 5))

    def test_place(self): # test place function
        grid = Grid()
        robot = Robot(grid)
        self.assertEqual(robot.place(3, 4, "NORTH"), (True, None))
        self.assertEqual(robot.x, 3)
        self.assertEqual(robot.y, 4)
        self.assertEqual(robot.f, "NORTH")
        self.assertEqual(robot.place(6, 7, "NORTH"), (False, INVALID_COORD_RANEG_ERR))

    def test_move(self): # test move function
        grid = Grid()
        robot = Robot(grid)
        robot.x = 3
        robot.y = 4
        robot.f = "EAST"
        self.assertEqual(robot.move(), (True, None))
        self.assertEqual(robot.x, 4)
        self.assertEqual(robot.y, 4)
        self.assertEqual(robot.f, "EAST")
        self.assertEqual(robot.move(), (False, INVALID_COORD_RANEG_ERR))

    def test_turn(self): # test turn function
        grid = Grid()
        robot = Robot(grid)
        robot.x = 3
        robot.y = 4
        robot.f = "SOUTH"
        robot.turn("RIGHT")
        self.assertEqual(robot.x, 3)
        self.assertEqual(robot.y, 4)
        self.assertEqual(robot.f, "WEST")
        robot.turn("LEFT")
        self.assertEqual(robot.f, "SOUTH")

    def test_report(self): # test report function
        grid = Grid()
        robot = Robot(grid)
        robot.x = 3
        robot.y = 4
        robot.f = "WEST"
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        robot.report()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Output: 3, 4, WEST\n") # print statement adds the newline character to the end of printed line

if __name__ == '__main__':
    unittest.main()