from typing import NamedTuple

class Point(NamedTuple):
    x:float
    y:float

p1 = Point(3, 4)
p2 = Point(3, 4)
print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p1 == p2: {p1 == p2}")
#print(type(p1))
#print(f"p1[0]: {p1[0]}, p1.x: {p1.x}")
#print(issubclass(Point, tuple))



print("================")

class Stock(NamedTuple):
    symbol: str
    current: float
    high: float
    low: float

    @property
    def middle(self) -> float:
        return (self.high + self.low) / 2

"""def middle(s):
    return (s.high + s.low) / 2"""

s = Stock("AAPL", 123.52, 137, 53.15)
print(f"The middle of {s.symbol} is {s.middle}")