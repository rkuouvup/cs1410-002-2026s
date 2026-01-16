import math

class Point:
    """
    Point class
    para x: x value in the coordinate
    para y: y value in the coordinate
    """
    numPoints = 0
    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        The initializer of the Point class
        """
        self.x = x
        self.y = y
        Point.numPoints += 1
    def move(self, x: float, y: float) -> None:
        """
        Move a point to another location
        """
        self.x = x
        self.y = y
    def reset(self) -> None:
        self.x = 0
        self.y = 0
    def calculate_distance(self, other: "Point") ->float:
        return math.hypot(self.x - other.x, self.y - other.y)
        # point1.calculate_distance(point2)
        # Point.calculate_distance(point1, point2)
    def __repr__(self) -> str:
        return f"<Point object (x: {self.x}, y:{self.y})>"
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


