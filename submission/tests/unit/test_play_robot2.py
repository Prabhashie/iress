"""
file name:      test_play_robot2.py
author:         Sachinthana Pathiranage
date created:   14/08/2022
purpose:        Unit tests for non-composite functions in play_robot2.py
version:        1.0
"""

# imports
import unittest
from src.play_robot2 import *
from utils.test_utils import *
from utils.log_msgs import *
from classes.robot import Robot
from classes.grid import Grid

class TestPlayRobot2(unittest.TestCase):
    def test_get_processed_input(self): # test get_processed_input function
        stub_stdin(self, ' PLACE  1, 0, NORTH ')
        comm = get_processed_input()
        self.assertEqual(len(comm), 2)

        stub_stdin(self, 'MOVE ')
        comm = get_processed_input()
        self.assertEqual(len(comm), 1)
    
    def test_get_processed_args(self): # test get_processed_args function
        args = "1, 0, NORTH"
        newArgs = get_processed_args(args)
        self.assertEqual(len(newArgs), 3)

        args = ", , "
        newArgs = get_processed_args(args)
        self.assertEqual(len(newArgs), 0)

        args = "1, ,"
        newArgs = get_processed_args(args)
        self.assertEqual(len(newArgs), 1)

    def test_validate_args(self): # test validate_args function
        args = [3, 4, "NoRtH"]
        isValid, errStr, x, y, f = validate_args(args)
        self.assertEqual(isValid, True)
        self.assertEqual(errStr, '')
        self.assertEqual(type(x), int)
        self.assertEqual(type(y), int)
        self.assertEqual(f, "NORTH")

        args = ['a', 'b', "North"]
        isValid, errStr, x, y, f = validate_args(args)
        self.assertEqual(isValid, False)
        self.assertEqual(errStr, UNEXPECTED_TYPE_ERR + " x coordinate should be an integer.")
        self.assertEqual(x, None)
        self.assertEqual(y, None)
        self.assertEqual(f, None)

        args = [3, 'b', "North West"]
        isValid, errStr, x, y, f = validate_args(args)
        self.assertEqual(isValid, False)
        self.assertEqual(errStr, UNEXPECTED_TYPE_ERR + " y coordinate should be an integer.")
        self.assertEqual(x, 3)
        self.assertEqual(y, None)
        self.assertEqual(f, None)

        args = [6, 7, "South West"]
        isValid, errStr, x, y, f = validate_args(args)
        self.assertEqual(isValid, False)
        self.assertEqual(errStr, INVALID_DIRECTION_ERR + " Valid directions are [NORTH, SOUTH, EAST, WEST].")
        self.assertEqual(x, 6)
        self.assertEqual(y, 7)
        self.assertEqual(f, None)

if __name__ == '__main__':
    unittest.main()