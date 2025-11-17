class Map():
    def __init__(self,width,height):
        self.map =[]
        __row =[]
        for j in range(width):
            __row.append("x")
        for i in range(height):
            self.map.append(__row)
        return None

    def return_map(self):
        return self.map
        #for row in self.map:
        #    print(row)
field = Map(10,20)
print(len(field.return_map()))