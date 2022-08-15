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
    def setUp(self):
        self.grid = Grid()

    def test_init(self): # test init function
        self.assertEqual(self.grid.xDim, 5)
        self.assertEqual(self.grid.yDim, 5)

    def test_change_dimX(self): # test changeDimX function
        self.grid.change_dimX(7)
        self.assertEqual(self.grid.xDim, 7)
        self.assertEqual(self.grid.yDim, 5)

    def test_change_dimX(self): # test changeDimY function
        self.grid.change_dimY(7)
        self.assertEqual(self.grid.xDim, 5)
        self.assertEqual(self.grid.yDim, 7)

if __name__ == '__main__':
    unittest.main()