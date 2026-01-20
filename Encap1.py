class MyClass:
    def __init__(self, x:str = "public attribute", 
                        y:str = "suggested private",
                        z:str = "private access"):
        self.x = x
        self._y = y
        self.__z = z
    def get_y(self) -> str:
        return self._y
    def set_y(self, value:str) -> None:
        self._y = value

def main() -> None:
    obj = MyClass("hello", "world")
    print(obj.x)
    #print(obj._y)  # Not recommended
    print(obj.get_y())  # Recommended
    obj.set_y("Python")
    print(obj.get_y())

    print(obj._MyClass__z)  # Not recommended

if __name__ == "__main__":
    main()
