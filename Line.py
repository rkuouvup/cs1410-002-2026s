from Point import Point
#.  Module Name.  Class Name

class Line:
    def __init__(self, start:"Point", end:"Point") -> None:
        self.start = start
        self.end = end

    def length(self) -> float:
        return self.start.calculate_distance(self.end)


def main():
    p1 = Point(5, 4)

    a = 3
    b = "hello"
    print("a value is " + str(a))
    print(b)
    print(p1)
    print("p1 is located at " + str(p1))


    p2 = Point(2, 3)
    p3 = Point()
    print(p1.calculate_distance(p2))

    print(f"p1.x: {p1.x}")
    print(f"p2.x: {p2.x}")
    print(f"p3.x: {p3.x}")
    p1.z = 10
    print(p1.z)

    line1 = Line(p1, p2)
    print(line1.length())

if __name__ == "__main__":
    main()