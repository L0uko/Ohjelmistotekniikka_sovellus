import unittest
from logic.map import Map
from logic.tetromino import Tetromino


class TestMap(unittest.TestCase):
    def setUp(self):
        self._field = Map(10, 20)

    def test_map_right_size(self):
        self.assertEqual(len(self._field.return_map()), 20)
        for row in self._field.return_map():
            self.assertEqual(len(row), 10)

    def test_spawn_i(self):
        self._current_piece = Tetromino(self._field)
        self.assertEqual(self._current_piece.spawn(0), True)

    def test_spawn_o(self):
        self._current_piece = Tetromino(self._field)
        self.assertEqual(self._current_piece.spawn(1), True)

    def test_spawn_t(self):
        self._current_piece = Tetromino(self._field)
        self.assertEqual(self._current_piece.spawn(2), True)

    def test_spawn_s(self):
        self._current_piece = Tetromino(self._field)
        self.assertEqual(self._current_piece.spawn(3), True)

    def test_spawn_z(self):
        self._current_piece = Tetromino(self._field)
        self.assertEqual(self._current_piece.spawn(4), True)

    def test_spawn_j(self):
        self._current_piece = Tetromino(self._field)
        self.assertEqual(self._current_piece.spawn(5), True)

    def test_spawn_l(self):
        self._current_piece = Tetromino(self._field)
        self.assertEqual(self._current_piece.spawn(6), True)

class TestRotate(unittest.TestCase):
    def setUp(self):
        self._field = Map(10, 20)
        self._tetromino = Tetromino(self._field)

    def test_rotate_i(self):
        self._block =  [
                        [1,1,1,1],
        ]
        self.assertEqual(self._tetromino.rotate_block(self._block),
                         [
                        [1],
                        [1],
                        [1],
                        [1]
                         ])

    def test_rotate_t(self):
        self._block =  [
                        [0, 1, 0],
                        [1, 1, 1]
        ]
        self.assertEqual(self._tetromino.rotate_block(self._block),
                         [
                        [1,0],
                        [1,1],
                        [1,0]
                         ])

    def test_rotate_o(self):
        self._block =  [
                    [1, 1],
                    [1, 1]
        ]
        self.assertEqual(self._tetromino.rotate_block(self._block),
                         [
                        [1,1],
                        [1,1]
                         ])
    
    def test_rotate_s(self):
        self._block =  [
                    [0, 1, 1],
                    [1, 1, 0]
        ]
        self.assertEqual(self._tetromino.rotate_block(self._block),
                         [
                        [1,0],
                        [1,1],
                        [0,1]
                         ])

    def test_rotate_s_faulty(self):
        self._block =  [
                    [0, 1, 0],
                    [1, 1, 0]
        ]
        self.assertNotEqual(self._tetromino.rotate_block(self._block),
                         [
                        [1,0],
                        [1,1],
                        [0,1]
                         ])

    def test_rotate_z(self):
        self._block =  [
                    [1, 1, 0],
                    [0, 1, 1]
        ]
        self.assertEqual(self._tetromino.rotate_block(self._block),
                         [
                        [0,1],
                        [1,1],
                        [1,0]
                         ])
        
    def test_rotate_j(self):
        self._block =  [
                    [1, 0, 0],
                    [1, 1, 1]
        ]
        self.assertEqual(self._tetromino.rotate_block(self._block),
                         [
                        [1,1],
                        [1,0],
                        [1,0]
                         ])
        
    def test_rotate_l(self):
        self._block =  [
                    [0, 0, 1],
                    [1, 1, 1]
        ]
        self.assertEqual(self._tetromino.rotate_block(self._block),
                         [
                        [1,0],
                        [1,0],
                        [1,1]
                         ])
        