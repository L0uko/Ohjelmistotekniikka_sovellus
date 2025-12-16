import time
import pygame
from game import Game

class Loop:
    def __init__(self, game: Game):
        """The main loop for the gameplay

        Args:
            field (Map): Map-type object
            ui (): The userinteface 
        """
        self._game = game
        self._field = game._field
        self._ui = game._ui
        self.running = True

    def start(self):
        """Initialises pygame and has the gameloop"""
        pygame.init()
        self._ui.init_window(self._field.columns(), self._field.rows())

        # Initial piece
        if not self._game._piece.spawn():
            self.running = False

        while self.running:
            self._game._clock.tick(60)  # limit to 60 FPS
            self._game.process_input()
            self._game.gravity_step(self._game._clock.get_ticks())
            self._game.draw()
            self.running = self._game.check_if_running()


        # Game over screen
        self._ui.draw_game_over(self._game._score)
        pygame.display.flip()
        # Pause briefly then exit
        time.sleep(1)