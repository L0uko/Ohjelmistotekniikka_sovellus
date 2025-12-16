
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
