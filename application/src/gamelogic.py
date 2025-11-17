#file for the game logic

class Map():
    def __init__(self,width,height):
        self.map =[]
        __row =[]
        for j in range(width):
            __row.append("x")
        for i in range(height):
            self.map.append(__row)

    def print_map(self):
        print(self.map)
        #for row in self.map:
        #    print(row)
field = Map(10,20)
field.print_map()


"""[
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"],
        ]"""