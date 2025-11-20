import unittest
from gamelogic import Map


class TestMap(unittest.TestCase):
    def setUp(self):
        self.field = Map(10, 20)

    def test_map_right_size(self):
        self.assertEqual(len(self.field.return_map()), 20)
        for row in self.field.return_map():
            self.assertEqual(len(row), 10)
