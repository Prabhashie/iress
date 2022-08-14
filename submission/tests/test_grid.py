"""
file name:      test_grid.py
author:         Sachinthana Pathiranage
date created:   14/08/2022
purpose:        Unit tests for Grid class
version:        1.0
"""

# imports
import unittest
from classes.grid import Grid

class TestGrid(unittest.TestCase):
    def test_init(self): # test init function
        grid = Grid()
        self.assertEqual(grid.xDim, 5)
        self.assertEqual(grid.yDim, 5)

    def test_changeDims(self): # test changeDims function
        grid = Grid()
        grid.changeDims(7,7)
        self.assertEqual(grid.xDim, 7)
        self.assertEqual(grid.yDim, 7)

if __name__ == '__main__':
    unittest.main()