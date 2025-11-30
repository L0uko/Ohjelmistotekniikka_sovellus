import unittest
from gamelogic import Map


class TestMap(unittest.TestCase):
    def setUp(self):
        self.field = Map(10, 20)

    def test_map_right_size(self):
        self.assertEqual(len(self.field.return_map()), 20)
        for row in self.field.return_map():
            self.assertEqual(len(row), 10)

    def test_place_i(self):
        block_i = self.field.return_block_list()[0]
        self.field.new_block(0,0,block_i)
        self.assertEqual(self.field.return_map()[0], [1,1,1,1,0,0,0,0,0,0])

    def test_place_o(self):
        block_o = self.field.return_block_list()[1]
        self.field.new_block(0,0,block_o)
        self.assertEqual(self.field.return_map()[0], [1,1,0,0,0,0,0,0,0,0])
        self.assertEqual(self.field.return_map()[1], [1,1,0,0,0,0,0,0,0,0])

    def test_place_t(self):
        block_t = self.field.return_block_list()[2]
        self.field.new_block(0,0,block_t)
        self.assertEqual(self.field.return_map()[0], [0,1,0,0,0,0,0,0,0,0])
        self.assertEqual(self.field.return_map()[1], [1,1,1,0,0,0,0,0,0,0])

    def test_place_s(self):
        block_s = self.field.return_block_list()[3]
        self.field.new_block(0,0,block_s)
        self.assertEqual(self.field.return_map()[0], [0,1,1,0,0,0,0,0,0,0])
        self.assertEqual(self.field.return_map()[1], [1,1,0,0,0,0,0,0,0,0])

    def test_place_z(self):
        block_z = self.field.return_block_list()[4]
        self.field.new_block(0,0,block_z)
        self.assertEqual(self.field.return_map()[0], [1,1,0,0,0,0,0,0,0,0])
        self.assertEqual(self.field.return_map()[1], [0,1,1,0,0,0,0,0,0,0])

    def test_place_j(self):
        block_j = self.field.return_block_list()[5]
        self.field.new_block(0,0,block_j)
        self.assertEqual(self.field.return_map()[0], [1,0,0,0,0,0,0,0,0,0])
        self.assertEqual(self.field.return_map()[1], [1,1,1,0,0,0,0,0,0,0])

    def test_place_l(self):
        block_l = self.field.return_block_list()[6]
        self.field.new_block(0,0,block_l)
        self.assertEqual(self.field.return_map()[0], [0,0,1,0,0,0,0,0,0,0])
        self.assertEqual(self.field.return_map()[1], [1,1,1,0,0,0,0,0,0,0])