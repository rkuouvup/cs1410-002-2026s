import math

class Point:
    numPoints = 0
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y
        Point.numPoints += 1
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    def reset(self) -> None:
        self.x = 0
        self.y = 0
    def calculate_distance(self, other: "Point") ->float:
        return math.hypot(self.x - other.x, self.y - other.y)

def main():
    a = 3
    b = "Hello"
    p1 = Point(5, 4)
    p1.move(10, 10)
    p2 = Point(2, 3)
    p3 = Point()
    print(p1.calculate_distance(p2))

    print(f"p1.x: {p1.x}")
    print(f"p2.x: {p2.x}")
    print(f"p3.x: {p3.x}")
    p1.z = 10
    print(p1.z)

if __name__ == "__main__":
    main()