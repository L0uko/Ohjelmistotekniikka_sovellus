class Map():
    def __init__(self, width, height):
        self._map = []
        __row = []
        for j in range(width):
            __row.append("x")
        for i in range(height):
            self._map.append(__row)
        return None

    def return_map(self):
        return self._map

    def return_map_str(self):
        _mapstring = str(self._map)
        _mapstring = _mapstring.replace('], ',']\n')
        _mapstring = _mapstring.replace('[',"")
        _mapstring = _mapstring.replace(']',"")
        _mapstring = _mapstring.replace("'","")
        _mapstring = _mapstring.replace(','," ")
        return _mapstring
        # for row in self.map:
        #    print(row)

class Clock():
    def __init__(self):
        pass