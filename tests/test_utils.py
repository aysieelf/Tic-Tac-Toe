import unittest

from src.utils import get_cell_from_mouse


class UtilsShould(unittest.TestCase):
    def test_getCellFromMouse_returnsRowCol(self):
        self.assertEqual((0, 0), get_cell_from_mouse((0, 0)))
        self.assertEqual((0, 1), get_cell_from_mouse((100, 0)))
        self.assertEqual((0, 2), get_cell_from_mouse((200, 0)))
        self.assertEqual((1, 0), get_cell_from_mouse((0, 100)))
        self.assertEqual((1, 1), get_cell_from_mouse((100, 100)))
        self.assertEqual((1, 2), get_cell_from_mouse((200, 100)))
        self.assertEqual((2, 0), get_cell_from_mouse((0, 200)))
        self.assertEqual((2, 1), get_cell_from_mouse((100, 200)))
        self.assertEqual((2, 2), get_cell_from_mouse((200, 200)))
