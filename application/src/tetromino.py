import random
from map import Map

class Tetromino:

    def __init__(self, field: Map):
        """Controls the current falling Tetromino

        Args:
            field (Map): Input the map
        """
        self._field = field
        self._shape_index = 0
        self._block = None
        self._current_bag = [0,1,2,3,4,5,6]
        self._current_bag_index = 0
        self._top_row = 0
        self._left_column = 0
        self._color = (255, 255, 255)

    def return_block_as_list(self):
        """Returns the block as a list

        Returns:
            list: 2D matrix
        """
        return self._block

    def return_block_position(self):
        """Returns blocks position as a tuple (top_row,left_column)
        """
        return (self._top_row,self._left_column)

    def return_color(self):
        """returns color

        Returns:
            tuple: RGB color value
        """
        return self._color

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
            # Use the current bag to ensure all pieces appear before repeating
            if self._current_bag_index >= len(self._current_bag):
                random.shuffle(self._current_bag)
                self._current_bag_index = 0
            self._shape_index = self._current_bag[self._current_bag_index]
            self._current_bag_index += 1
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
                    if self._field.in_bounds(r, c) and self._field.get_cell(r, c) != 0:
                        self._field.set_cell(r, c, 0)

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
