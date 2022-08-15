"""
file name:      test_play_robot1.py
author:         Sachinthana Pathiranage
date created:   14/08/2022
purpose:        Integration tests for play_robot1.py
version:        1.0
"""

# imports
import unittest
from unittest import mock
from io import StringIO
from src import play_robot1
from utils.test_utils import *
from utils.log_msgs import *

class TestPlayRobot1(unittest.TestCase):
    def setUp(self):
        play_robot1.GRID_X = 5
        play_robot1.GRID_Y = 5

    def test_redefine_grid1(self): # dimensions correctly set but with incorrect values at first
        with mock.patch('builtins.input') as mockInput:
            with mock.patch('sys.stdout', new_callable = StringIO) as mockOutput:
                mockInput.side_effect = ['a', '6', 'b', '7']
                play_robot1.redefine_grid()

                self.assertTrue(INVALID_DIMENSION_ERR in mockOutput.getvalue())
                self.assertTrue(NEW_GRID_DIMENSIONS_SET_INFO in mockOutput.getvalue())
                self.assertTrue(INVALID_DIMENSION_ERR in mockOutput.getvalue())
                self.assertTrue(NEW_GRID_DIMENSIONS_SET_INFO in mockOutput.getvalue())
                self.assertEqual(play_robot1.GRID_X, 6)
                self.assertEqual(play_robot1.GRID_Y, 7)
    
    def test_redefine_grid2(self): # only one dimension is set
        with mock.patch('builtins.input') as mockInput:
            with mock.patch('sys.stdout', new_callable = StringIO) as mockOutput:
                mockInput.side_effect = ['6', 'Q']
                play_robot1.redefine_grid()

                self.assertTrue(NEW_GRID_DIMENSIONS_SET_INFO in mockOutput.getvalue())
                self.assertTrue(PARAM_NOT_SET_INFO + " Parameter: Grid y dimension." in mockOutput.getvalue())
                self.assertEqual(play_robot1.GRID_X, 6)
                self.assertEqual(play_robot1.GRID_Y, 5)
        
    def test_play_game1(self): # quit play at the beginning
        with mock.patch('builtins.input') as mockInput:
            with mock.patch('sys.stdout', new_callable = StringIO) as mockOutput:
                mockInput.side_effect = ['Q']
                play_robot1.play_game()

                self.assertTrue(EXIT_PROGRAM_INFO in mockOutput.getvalue())

    def test_play_game2(self): # inavlid commands
        with mock.patch('builtins.input') as mockInput:
            with mock.patch('sys.stdout', new_callable = StringIO) as mockOutput:
                mockInput.side_effect = ["", "Hello There", "Q"]
                play_robot1.play_game()

                self.assertTrue(INVALID_COMMAND_FORMAT_ERR in mockOutput.getvalue())
                self.assertTrue(INVALID_COMMAND_ERR in mockOutput.getvalue())
                self.assertTrue(EXIT_PROGRAM_INFO in mockOutput.getvalue())
    
    def test_play_game3(self): # out of grid place
        with mock.patch('builtins.input') as mockInput:
            with mock.patch('sys.stdout', new_callable = StringIO) as mockOutput:
                mockInput.side_effect = ["PLACE 5,5,NORTH", "Q"]
                play_robot1.play_game()

                self.assertTrue(INVALID_COORD_RANEG_ERR in mockOutput.getvalue())
    
    def test_play_game4(self): # invalid singular command
        with mock.patch('builtins.input') as mockInput:
            with mock.patch('sys.stdout', new_callable = StringIO) as mockOutput:
                mockInput.side_effect = ["PLACE", "Q"]
                play_robot1.play_game()

                self.assertTrue(INVALID_COMMAND_ERR in mockOutput.getvalue())
    
    def test_play_game5(self): # robot not placed on grid yet
        with mock.patch('builtins.input') as mockInput:
            with mock.patch('sys.stdout', new_callable = StringIO) as mockOutput:
                mockInput.side_effect = ["MOVE", "Q"]
                play_robot1.play_game()

                self.assertTrue(ROBOT_NOT_PLACED_ERR in mockOutput.getvalue())

    def test_play_game6(self): # correct inputs scenario 1
        with mock.patch('builtins.input') as mockInput:
            with mock.patch('sys.stdout', new_callable = StringIO) as mockOutput:
                mockInput.side_effect = ["PLACE 0,0,NORTH", "MOVE", "REPORT", "Q"]
                play_robot1.play_game()

                self.assertTrue("Output: 0, 1, NORTH" in mockOutput.getvalue())

    def test_play_game7(self): # correct inputs scenario 2
        with mock.patch('builtins.input') as mockInput:
            with mock.patch('sys.stdout', new_callable = StringIO) as mockOutput:
                mockInput.side_effect = ["PLACE 0,0,NORTH", "LEFT", "REPORT", "Q"]
                play_robot1.play_game()

                self.assertTrue("Output: 0, 0, WEST" in mockOutput.getvalue())

    def test_play_game8(self): # correct inputs scenario 3
        with mock.patch('builtins.input') as mockInput:
            with mock.patch('sys.stdout', new_callable = StringIO) as mockOutput:
                mockInput.side_effect = ["PLACE 1,2,EAST", "MOVE", "MOVE", "LEFT", "MOVE", "REPORT", "Q"]
                play_robot1.play_game()

                self.assertTrue("Output: 3, 3, NORTH" in mockOutput.getvalue())


if __name__ == '__main__':
    unittest.main()