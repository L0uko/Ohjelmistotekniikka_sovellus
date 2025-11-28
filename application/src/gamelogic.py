from pprint import pprint
import time


class Map():
    def __init__(self, rows, columns):
        self._map = []
        for _ in range(columns):
            __row = []
            for _ in range(rows):
                __row.append(0)

            self._map.append(__row)
        self.block_t = [
            [0, 1, 0],
            [1, 1, 1]
        ]
        self.block_l = [
            [1, 0],
            [1, 0],
            [1, 1]
        ]
        # possible_blocks = [self.block_t]

    def return_map(self):
        return self._map

    def return_map_str(self):
        _mapstring = str(self._map)
        _mapstring = _mapstring.replace('], ', ']\n')
        _mapstring = _mapstring.replace('[', "")
        _mapstring = _mapstring.replace(']', "")
        _mapstring = _mapstring.replace("'", "")
        _mapstring = _mapstring.replace(',', " ")
        return _mapstring
        # for row in self.map:
        #    print(row)

    def new_block(self, row, column):
        for i_r, r in enumerate(self.block_t):
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
