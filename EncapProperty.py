class Circle:
    def __init__(self, radius:float) -> None:
        self._radius = radius
    def _get_radius(self) -> float:
        return self._radius
    def _set_radius(self, value) -> None:
        self._radius = value
    def _del_radius(self) -> None:
        del self._radius
    radius = property(fget = _get_radius,
                      fset = _set_radius,
                      fdel = _del_radius,
                      doc="The radius property")



def main() -> None:
    c1 = Circle(42.0)
    print(c1.radius)
    c1.radius = 100.0
    print(c1.radius)
    del c1.radius
    #print(c1.radius)
    help(c1)

if __name__ == "__main__":
    main()