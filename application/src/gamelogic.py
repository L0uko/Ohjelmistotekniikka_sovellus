import random
import time
import userinterface


class Map():
    def __init__(self, rows, columns):
        self._map = []
        for _ in range(columns):
            __row = []
            for _ in range(rows):
                __row.append(0)

            self._map.append(__row)

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

    def return_map(self):
        return self._map

    def return_block_list(self):
        """ Returns blocklist in order I O T S Z J L """
        return self._possible_blocks

    def return_map_str(self):
        _mapstring = str(self._map)
        _mapstring = _mapstring.replace('], ', ']\n')
        _mapstring = _mapstring.replace('[', "")
        _mapstring = _mapstring.replace(']', "")
        _mapstring = _mapstring.replace("'", "")
        _mapstring = _mapstring.replace(',', " ")
        return _mapstring


    def new_block(self, row, column, block):
        for i_r, r in enumerate(block):
            print("column:", r)
            for i_c, c in enumerate(r):
                print("row", c)
                if c == 1:  # only place filled cells
                    self._map[row + i_r][column + i_c] = 1

class Clock():
    def __init__(self):
        while True:
            # check_if_moved()
            # check_if_rotated()
            # check_piece_spot()
            # check_if_row()
            # update_map()
            time.sleep(0.1)
