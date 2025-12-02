import unittest
import gamelogic


class TestMap(unittest.TestCase):
    def setUp(self):
        self.field = gamelogic.Map(10, 20)

    def test_map_right_size(self):
        self.assertEqual(len(self.field.return_map()), 20)
        for row in self.field.return_map():
            self.assertEqual(len(row), 10)

    def test_place_i(self):
        self.current_piece = gamelogic.CurrentPiece(self.field)
        self.assertEqual(self.current_piece.spawn(0), True)

    def test_place_o(self):
        self.current_piece = gamelogic.CurrentPiece(self.field)
        self.assertEqual(self.current_piece.spawn(1), True)

    def test_place_t(self):
        self.current_piece = gamelogic.CurrentPiece(self.field)
        self.assertEqual(self.current_piece.spawn(2), True)

    def test_place_s(self):
        self.current_piece = gamelogic.CurrentPiece(self.field)
        self.assertEqual(self.current_piece.spawn(3), True)

    def test_place_z(self):
        self.current_piece = gamelogic.CurrentPiece(self.field)
        self.assertEqual(self.current_piece.spawn(4), True)

    def test_place_j(self):
        self.current_piece = gamelogic.CurrentPiece(self.field)
        self.assertEqual(self.current_piece.spawn(5), True)

    def test_place_l(self):
        self.current_piece = gamelogic.CurrentPiece(self.field)
        self.assertEqual(self.current_piece.spawn(6), True)
