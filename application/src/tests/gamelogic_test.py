import unittest

from gamelogic import Map

class TestMap(unittest.TestCase):
    def setUp(self):
        self.field = Map(10,20)
    def test_map_right_size(self):
        self.field.print_map()
        self.assertEqual(self.field.print_map(),"""[
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ]""")
