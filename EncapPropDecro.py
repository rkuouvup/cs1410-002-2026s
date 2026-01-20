class Circle:
    def __init__(self, radius:float) -> None:
        self._radius = radius
    @property
    def radius(self) -> float:
        return self._radius
    @radius.setter
    def radius(self, value:float) -> None:
        self._radius = value
    @radius.deleter
    def radius(self) -> None:
        del self._radius



def main() -> None:
    c1 = Circle(42.0)
    print(c1.radius)
    c1.radius = 100.0
    print(c1.radius)
    del c1.radius
    #print(c1.radius)
    """help(c1)"""

if __name__ == "__main__":
    main()