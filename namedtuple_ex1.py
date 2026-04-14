from collections import namedtuple

#Point = namedtuple("Point", "x y")
Point = namedtuple("Point", ["x", "y"])
p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1)
print(type(p1))
print(f"p1[0]: {p1[0]}, p1.x: {p1.x}")
#p1.x = 100
print(issubclass(Point, tuple))

print("======================")

class PointOrdinary:
    def __init__(self, x:int=0, y:int=0):
        self.x = x
        self.y = y

po1 = PointOrdinary(3, 4)
po2 = PointOrdinary(3, 4)
print(f"po1: ({po1.x}, {po1.y})")
#print(type(po1))
print(f"po2: ({po2.x}, {po2.y})")
print(po1)
print(po2)
print(f"po1 == po2: {po1 == po2}")
print(f"p1 == p2: {p1 == p2}")