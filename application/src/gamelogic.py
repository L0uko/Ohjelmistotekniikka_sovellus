import random
import time
import pygame
import userinterface


class Map:
    def __init__(self, rows, columns):
        """Makes the map object

        Args:
            rows (int): amount of rows
            columns (int): amount of columns
        """
        self._map = []
        self._rows = rows
        self._columns = columns
        for _ in range(columns):
            __col = []
            for _ in range(rows):
                __col.append(0)
            self._map.append(__col)
        self._block_i = [
            [1, 1, 1, 1]
        ]

        self._block_o = [
            [1, 1],
            [1, 1]
        ]

        self._block_t = [
            [0, 1, 0],
            [1, 1, 1]
        ]

        self._block_s = [
            [0, 1, 1],
            [1, 1, 0]
        ]

        self._block_z = [
            [1, 1, 0],
            [0, 1, 1]
        ]

        self._block_j = [
            [1, 0, 0],
            [1, 1, 1]
        ]

        self._block_l = [
            [0, 0, 1],
            [1, 1, 1]
        ]

        self._possible_blocks = [
            self._block_i,
            self._block_o,
            self._block_t,
            self._block_s,
            self._block_z,
            self._block_j,
            self._block_l
        ]

        self._colors = [
            (0, 255, 255),  # I
            (255, 255, 0),  # O
            (128, 0, 128),  # T
            (0, 255, 0),    # S
            (255, 0, 0),    # Z
            (0, 0, 255),    # J
            (255, 165, 0),  # L
        ]
        """ Colors per shape index (I,O,T,S,Z,J,L) """

    def rows(self):
        """ return amount of rows int """
        return self._rows

    def columns(self):
        """ returns amount of columns int """
        return self._columns

    def return_map(self):
        """ Returns the map in matrix formation """
        return self._map

    def return_block_list(self):
        """ Returns blocklist in order I O T S Z J L """
        return self._possible_blocks
    # Copilot code starts from here

    def color_for_index(self, idx):
        """ returns color from the wanted index"""
        return self._colors[idx % len(self._colors)]

    # --- Grid helpers (remember: storage is map[col][row]) ---

    def in_bounds(self, r, c):
        """ checks if in bounds """
        return 0 <= r < self._rows and 0 <= c < self._columns

    def get_cell(self, row, column):
        """ Returns the content of the wanted cell """
        return self._map[column][row]

    def set_cell(self, r, c, val):
        self._map[c][r] = val

    def clear_full_lines(self):
        """Clear full lines and collapse above."""
        cleared = 0
        r = self._rows - 1
        while r >= 0:
            full = True
            for c in range(self._columns):
                if self._map[c][r] == 0:
                    full = False
                    break
            if full:
                cleared += 1
                # Shift everything above down
                for rr in range(r, 0, -1):
                    for cc in range(self._columns):
                        self._map[cc][rr] = self._map[cc][rr - 1]
                # Clear top row
                for cc in range(self._columns):
                    self._map[cc][0] = 0
                # stay on same r to check new line at this index
            else:
                r -= 1
        return cleared


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

class Tetromino:

    def __init__(self, field: Map):
        """Controls the current falling Tetromino

        Args:
            field (Map): Input the map
        """
        self._field = field
        self._shape_index = 0
        self._block = None
        self._top_row = 0
        self._left_column = 0
        self._color = (255, 255, 255)

    def spawn(self, shape_index=None):
        """spawns a random tetromino or a from a chosen index

        Args:
            shape_index (int, optional): index of the tetromino. Defaults to None.

        Returns:
            Bool: True if placed \n
            False if not placed
        """
        blocks = self._field.return_block_list()
        # If caller provides shape_index, use it; otherwise random
        if shape_index is None:
            self._shape_index = random.randint(0, len(blocks) - 1)
        else:
            # Clamp to valid range
            self._shape_index = max(0, min(shape_index, len(blocks) - 1))

        base = blocks[self._shape_index]

        # Random rotation to add variety
        rot_count = random.randint(0, 3)
        self._block = base
        for _ in range(rot_count):
            self._block = self.rotate_block()

        self._color = self._field.color_for_index(self._shape_index)

        # Center horizontally
        width = len(self._block[0])
        self._left_column = (self._field.columns() - width) // 2
        self._top_row = 0

        # If can't place at spawn -> game over condition
        return self.can_place(self._block, self._top_row, self._left_column)

    # --- Piece operations ---

    def rotate_block(self):
        """Rotate block matrix clockwise."""
        # Transpose and reverse rows
        return [list(reversed(col)) for col in zip(*self._block)]

    def can_place(self, block, top_row, left_column):
        """Check if block fits with no collision at (top_r, left_c)."""
        for index_row, row in enumerate(block):
            for index_column, value in enumerate(row):
                if value == 0:
                    continue
                new_row = top_row + index_row
                new_column = left_column + index_column
                if not self._field.in_bounds(new_row, new_column):
                    return False
                if self._field.get_cell(new_row, new_column) != 0:
                    return False
        return True

    def clear_block(self, block, top_r, left_c):
        """Erase block from grid (useful for preview ghosts)."""
        for i_r, row in enumerate(block):
            for i_c, v in enumerate(row):
                if v == 1:
                    r = top_r + i_r
                    c = left_c + i_c
                    if self.in_bounds(r, c) and self.get_cell(r, c) != 0:
                        self.set_cell(r, c, 0)

    def try_move(self, amount_of_rows, amount_of_columns):
        """Moves the current piece the amount of rows and columns specified

        Args:
            d_r (int): amount of rows moved
            d_c (int): amount of columns moved

        Returns:
            Bool: True if placed \n
            False if not placed
        """
        new_row = self._top_row + amount_of_rows
        new_column = self._left_column + amount_of_columns
        if self.can_place(self._block, new_row, new_column):
            self._top_row = new_row
            self._left_column = new_column
            return True
        return False

    def try_rotate(self):
        """Tries to rotates the tetromino clockwise

        Returns:
            Bool: True if placed \n
            False if not placed
        """
        rotated = self.rotate_block()
        # Wall-kick attempts (simple): try same col, then +/-1 shift
        for kick in [(0, 0), (0, -1), (0, 1), (0, -2), (0, 2)]:
            nr = self._top_row + kick[0]
            nc = self._left_column + kick[1]
            if self.can_place(rotated, nr, nc):
                self._block = rotated
                self._top_row = nr
                self._left_column = nc
                return True
        return False

    def hard_drop(self):
        """Does a hard drop
        """
        while self.try_move(1, 0):
            pass

    def place_block(self, block, top_r, left_c, val):
        """Write block cells to grid with value val (color or 1)."""
        for i_r, row in enumerate(block):
            for i_c, v in enumerate(row):
                if v == 1:
                    self._field.set_cell(top_r + i_r, left_c + i_c, val)

    def lock_piece(self, block, top_r, left_c, color_value):
        """Permanently write piece with color_value to grid."""
        self.place_block(block, top_r, left_c, color_value)

    def lock_to_field(self):
        """Moves the current piece to a static piece
        """
        self.lock_piece(self._block, self._top_row, self._left_column, self._color)


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

    def draw(self):
        # Render static field
        self._ui.draw_grid(self._field)
        # Render current piece as overlay
        self._ui.draw_piece(self._piece._block, self._piece._top_row,
                            self._piece._left_column, self._piece._color)
        # HUD
        self._ui.draw_hud(score=self._score, level=self._level,
                          lines=self._lines_cleared)
        pygame.display.flip()

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