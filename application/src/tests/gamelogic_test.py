import unittest
from gamelogic import Map


class TestMap(unittest.TestCase):
    def setUp(self):
        self.field = Map(10, 20)

    def test_map_right_size(self):
        self.assertEqual(len(self.field.return_map()), 20)
        for row in self.field.return_map():
            self.assertEqual(len(row), 10)

    def test_place_t(self):
        block_t = self.field.return_block_list()[2]
        self.field.new_block(0,0,block_t)
        self.assertEqual(self.field.return_map()[0], [0,1,0,0,0,0,0,0,0,0])
        self.assertEqual(self.field.return_map()[1], [1,1,1,0,0,0,0,0,0,0])