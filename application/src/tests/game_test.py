import unittest 
from unittest.mock import MagicMock
from logic.game import Game
from logic.map import Map
from logic.tetromino import Tetromino
from userinterface import UI

class TestGame(unittest.TestCase):
    def setUp(self):
        self._field = Map(10, 20)
        self._ui = UI()
        self._game = Game(self._field, self._ui)
        self._game._piece = Tetromino(self._field)
        self._game._piece.can_place = MagicMock(return_value=True)

    def test_gravity_step_works(self):
        self._now_ticks = 1000
        self._game._last_fall_tick = 100
        self.assertTrue(self._game.gravity_step(self._now_ticks))

    def test_gravity_step_not_moved(self):
        self._now_ticks = 300
        self._game._last_fall_tick = 100
        self.assertFalse(self._game.gravity_step(self._now_ticks))