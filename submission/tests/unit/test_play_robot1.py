"""
file name:      test_play_robot1.py
author:         Sachinthana Pathiranage
date created:   14/08/2022
purpose:        Unit tests for non-composite functions in play_robot1.py
version:        1.0
"""

# imports
import unittest
from src.play_robot1 import *
from utils.test_utils import *
from utils.log_msgs import *

class TestPlayRobot1(unittest.TestCase):
    def test_get_processed_input(self): # test get_processed_input function
        stub_stdin(self, 'PLACE 1, 0, NORTH')
        comm = get_processed_input()
        self.assertEqual(len(comm), 2)

        stub_stdin(self, 'MOVE')
        comm = get_processed_input()
        self.assertEqual(len(comm), 1)

    def test_get_processed_args(self): # test get_processed_args function
        args = "1, 0, NORTH"
        newArgs = get_processed_args(args)
        self.assertEqual(len(newArgs), 3)

        args = "1, , 0, NORTH"
        newArgs = get_processed_args(args)
        self.assertEqual(len(newArgs), 0)

        args = "1, NORTH"
        newArgs = get_processed_args(args)
        self.assertEqual(len(newArgs), 0)

    def test_validate_args(self): # test validate_args function
        args = [3, 4, "North"]
        isValid, errStr, x, y, f = validate_args(args)
        self.assertEqual(isValid, True)
        self.assertEqual(errStr, '')
        self.assertEqual(type(x), int)
        self.assertEqual(type(y), int)
        self.assertEqual(f, "NORTH")

        args = ['a', 4, "North"]
        isValid, errStr, x, y, f = validate_args(args)
        self.assertEqual(isValid, False)
        self.assertEqual(errStr, UNEXPECTED_TYPE_ERR + " x coordinate should be an integer.")
        self.assertEqual(x, None)
        self.assertEqual(y, None)
        self.assertEqual(f, None)

        args = [3, 'b', "North"]
        isValid, errStr, x, y, f = validate_args(args)
        self.assertEqual(isValid, False)
        self.assertEqual(errStr, UNEXPECTED_TYPE_ERR + " y coordinate should be an integer.")
        self.assertEqual(x, 3)
        self.assertEqual(y, None)
        self.assertEqual(f, None)

        args = [3, 4, "South West"]
        isValid, errStr, x, y, f = validate_args(args)
        self.assertEqual(isValid, False)
        self.assertEqual(errStr, INVALID_DIRECTION_ERR + " Valid directions are [NORTH, SOUTH, EAST, WEST].")
        self.assertEqual(x, 3)
        self.assertEqual(y, 4)
        self.assertEqual(f, None)

    def test_valid_coords(self): # test valid_coords function
        self.assertTrue(valid_coords(3, 4))
        self.assertFalse(valid_coords(6, 7))

    def test_place(self): # test place function
        unprocessedArgs, x, y, f = "3, 4, EAST", 2, 3, "WEST"
        isValid, newX, newY, newF = place(unprocessedArgs, x, y, f)
        self.assertEqual(isValid, True)
        self.assertEqual(newX, 3)
        self.assertEqual(newY, 4)
        self.assertEqual(newF, "EAST")

        unprocessedArgs, x, y, f = "3, 4, SOUTH WEST", 2, 3, "WEST"
        stub_stdouts(self)
        isValid, newX, newY, newF = place(unprocessedArgs, x, y, f)
        self.assertEqual(sys.stdout.getvalue(), INVALID_DIRECTION_ERR + " Valid directions are [NORTH, SOUTH, EAST, WEST].\n")
        self.assertEqual(isValid, False)
        self.assertEqual(newX, 2)
        self.assertEqual(newY, 3)
        self.assertEqual(newF, "WEST")

        unprocessedArgs, x, y, f = "6, 7, EAST", 2, 3, "WEST"
        stub_stdouts(self)
        isValid, newX, newY, newF = place(unprocessedArgs, x, y, f)
        self.assertEqual(sys.stdout.getvalue(), INVALID_COORD_RANEG_ERR + "\n")
        self.assertEqual(isValid, False)
        self.assertEqual(newX, 2)
        self.assertEqual(newY, 3)
        self.assertEqual(newF, "WEST")

        unprocessedArgs, x, y, f = "3, , EAST", 2, 3, "WEST"
        stub_stdouts(self)
        isValid, newX, newY, newF = place(unprocessedArgs, x, y, f)
        self.assertEqual(sys.stdout.getvalue(), INVALID_ATTR_COUNT_ERR + "\n")
        self.assertEqual(isValid, False)
        self.assertEqual(newX, 2)
        self.assertEqual(newY, 3)
        self.assertEqual(newF, "WEST")

    def test_move(self): # test move function
        x, y, f = 2, 3, "WEST"
        isValid, newX, newY = move( x, y, f)
        self.assertEqual(isValid, True)
        self.assertEqual(newX, 1)
        self.assertEqual(newY, 3)

        x, y, f = 0, 3, "WEST"
        stub_stdouts(self)
        isValid, newX, newY = move( x, y, f)
        self.assertEqual(sys.stdout.getvalue(), INVALID_COORD_RANEG_ERR + "\n")
        self.assertEqual(isValid, False)
        self.assertEqual(newX, 0)
        self.assertEqual(newY, 3)

    def test_turn(self): # test turn function
        self.assertEqual(turn("SOUTH", "RIGHT"), "WEST")
        self.assertEqual(turn("WEST", "LEFT"), "SOUTH")

    def test_report(self): # test report function
        stub_stdouts(self)
        report(3, 4, "NORTH")
        self.assertEqual(sys.stdout.getvalue(), "Output: 3, 4, NORTH\n")

if __name__ == '__main__':
    unittest.main()