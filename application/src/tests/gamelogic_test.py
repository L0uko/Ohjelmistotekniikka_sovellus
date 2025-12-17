import unittest
from logic.map import Map
from logic.tetromino import Tetromino


class TestMap(unittest.TestCase):
    def setUp(self):
        self.field = Map(10, 20)

    def test_map_right_size(self):
        self.assertEqual(len(self.field.return_map()), 20)
        for row in self.field.return_map():
            self.assertEqual(len(row), 10)

    def test_spawn_i(self):
        self._current_piece = Tetromino(self.field)
        self.assertEqual(self._current_piece.spawn(0), True)

    def test_spawn_o(self):
        self._current_piece = Tetromino(self.field)
        self.assertEqual(self._current_piece.spawn(1), True)

    def test_spawn_t(self):
        self._current_piece = Tetromino(self.field)
        self.assertEqual(self._current_piece.spawn(2), True)

    def test_spawn_s(self):
        self._current_piece = Tetromino(self.field)
        self.assertEqual(self._current_piece.spawn(3), True)

    def test_spawn_z(self):
        self._current_piece = Tetromino(self.field)
        self.assertEqual(self._current_piece.spawn(4), True)

    def test_spawn_j(self):
        self._current_piece = Tetromino(self.field)
        self.assertEqual(self._current_piece.spawn(5), True)

    def test_spawn_l(self):
        self._current_piece = Tetromino(self.field)
        self.assertEqual(self._current_piece.spawn(6), True)
