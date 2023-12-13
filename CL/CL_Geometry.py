class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y


    def Plus(self, vector):
        pt = Point(0, 0)
        pt.add(vector)
        return pt

