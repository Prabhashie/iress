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
    def setUp(self):
        self.grid = Grid()
        self.robot = Robot(self.grid)

    def test_init(self): # test init function
        self.assertEqual(self.robot.x, None)
        self.assertEqual(self.robot.y, None)
        self.assertEqual(self.robot.f, None)
        self.assertIsInstance(self.robot.grid, Grid)
    
    def test_validCoords(self): # test validCoords function
        self.assertTrue(self.robot.validCoords(3, 4))
        self.assertFalse(self.robot.validCoords(6, 7))
        self.assertFalse(self.robot.validCoords(4, 5))
        self.assertFalse(self.robot.validCoords(5, 4))
        self.assertFalse(self.robot.validCoords(5, 5))

    def test_place(self): # test place function
        self.assertEqual(self.robot.place(3, 4, "NORTH"), (True, None))
        self.assertEqual(self.robot.x, 3)
        self.assertEqual(self.robot.y, 4)
        self.assertEqual(self.robot.f, "NORTH")
        self.assertEqual(self.robot.place(6, 7, "NORTH"), (False, INVALID_COORD_RANEG_ERR))

    def test_move(self): # test move function
        self.robot.x = 3
        self.robot.y = 4
        self.robot.f = "EAST"
        self.assertEqual(self.robot.move(), (True, None))
        self.assertEqual(self.robot.x, 4)
        self.assertEqual(self.robot.y, 4)
        self.assertEqual(self.robot.f, "EAST")
        self.assertEqual(self.robot.move(), (False, INVALID_COORD_RANEG_ERR))

    def test_turn(self): # test turn function
        self.robot.x = 3
        self.robot.y = 4
        self.robot.f = "SOUTH"
        self.robot.turn("RIGHT")
        self.assertEqual(self.robot.x, 3)
        self.assertEqual(self.robot.y, 4)
        self.assertEqual(self.robot.f, "WEST")
        self.robot.turn("LEFT")
        self.assertEqual(self.robot.f, "SOUTH")

    def test_report(self): # test report function
        self.robot.x = 3
        self.robot.y = 4
        self.robot.f = "WEST"
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        self.robot.report()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Output: 3, 4, WEST\n") # print statement adds the newline character to the end of printed line

if __name__ == '__main__':
    unittest.main()