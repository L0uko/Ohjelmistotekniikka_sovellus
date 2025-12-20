import pygame
import userinterface
from logic.tetromino import Tetromino
from logic.map import Map

class Clock:
    """
    Controls the ingame clock
    """

    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        self._clock.tick(fps)

    def get_ticks(self):
        return pygame.time.get_ticks()

class Game:
    def __init__(self, field: Map, ui: userinterface.UI):
        """Game object that has functions

        Args:
            field (Map): Map-type object
            ui (): The userinteface 
        """
        self._field = field
        self._ui = ui
        self._clock = Clock()
        self._last_fall_tick = 0
        self._fall_interval_ms = 800  # base fall speed
        self.running = True


        # Game state
        self._piece = Tetromino(self._field)
        self._level = 1
        self._lines_cleared = 0
        self._score = 0

    def check_if_running(self):
        return self.running

    def update_level_speed(self):
        """Updates the tetromino drop speed.\n
        every 10 lines, speed up by 10%
        """
        # Basic leveling: every 10 lines, speed up by 10%
        self._level = max(1, 1 + self._lines_cleared // 10) ###CHANGE TO 5 LINES
        self._fall_interval_ms = max(
            120, int(800 * (0.9 ** (self._level - 1))))

    def handle_lock_and_new(self):
        # Lock current piece
        self._piece.lock_to_field()
        # Clear lines
        cleared = self._field.clear_full_lines()
        if cleared > 0:
            # Classic scoring (simplified)
            # Single=100, Double=300, Triple=500, Tetris=800, scaled by level
            base_scores = {1: 100, 2: 300, 3: 500, 4: 800}
            self._score += base_scores.get(cleared,
                                           cleared * 100) * self._level
            self._lines_cleared += cleared
            self.update_level_speed()
        # Spawn next piece
        if not self._piece.spawn():
            # Game over
            self.running = False

    def process_input(self):
        """Goes through all of the possible inputs
        Ignore the pygame errors, it still works and I have no idea why they appear"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_LEFT:
                    self._piece.try_move(0, -1)
                elif event.key == pygame.K_RIGHT:
                    self._piece.try_move(0, 1)
                elif event.key == pygame.K_DOWN:
                    # soft drop
                    moved = self._piece.try_move(1, 0)
                    if not moved:
                        self.handle_lock_and_new()
                        self._last_fall_tick = self._clock.get_ticks()
                elif event.key == pygame.K_UP:
                    self._piece.try_rotate()
                elif event.key == pygame.K_SPACE:
                    # hard drop
                    self._piece.hard_drop()
                    self.handle_lock_and_new()
                    self._last_fall_tick = self._clock.get_ticks()

    def gravity_step(self, now_ticks):
        """ Makes the gravity working"""
        if now_ticks - self._last_fall_tick >= self._fall_interval_ms:
            moved = self._piece.try_move(1, 0)
            if not moved:
                self.handle_lock_and_new()
            self._last_fall_tick = now_ticks
            return True
        else:
            return False

    def return_score(self):
        """returns score

        Returns:
            int: Score
        """
        return self._score

    def draw(self):
        # Render static field
        self._ui.draw_grid(self._field)
        # Render current piece as overlay
        block_position =  self._piece.return_block_position()
        self._ui.draw_piece(
                            self._piece.return_block_as_list(),
                            block_position[0],
                            block_position[1],
                            self._piece.return_color()
                            )
        # HUD
        self._ui.draw_hud(score=self._score, level=self._level,
                          lines=self._lines_cleared)
        pygame.display.flip()

    def spawn_piece(self):
        return self._piece.spawn()
