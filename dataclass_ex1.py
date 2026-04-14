from dataclasses import dataclass

@dataclass(order=True)
class Stock:
    symbol: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0

class StockOrdinary:
    def __init__(self, name, current, high, low):
        self.name = name
        self.current = current
        self.high = high
        self.low = low

s1 = Stock("AAPL", 123.52, 137.98, 53.15)
print(s1)

#s.current = 130
#print(s)
s2 = Stock("AAPL", 130, 137.98, 53.15)
print(f"s1 == s2: {s1 == s2}")
print(f"s1 > s2: {s1 > s2}")

so1 = StockOrdinary("AAPL", 123.52, 137.98, 53.15)
so2 = StockOrdinary("AAPL", 123.52, 137.98, 53.15)
print(f"so1 == so2: {so1 == so2}")

s3 = Stock("FOO")
print(s3, low=5.5)