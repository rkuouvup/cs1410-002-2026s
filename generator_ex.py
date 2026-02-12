from typing import Iterator

class InfiniteSequence:
    def __init__(self) -> None:
        self._current:int = 0
    def __iter__(self) -> Iterator:
        return self
    def __next__(self) -> int:
        current:int = self._current
        self._current += 1
        return current * 2

def infinit_sequence():
    current = 0
    while True:
        yield current * 2
        current += 1

def main() -> None:
    s = InfiniteSequence()
    for i in range(5):
        print(next(s))
    print("=============")
    g = infinit_sequence()
    for i in range(5):
        print(next(g))
    print("==== List Comprehension =====")
    l = [num * 2 for num in range(5)]
    print(l)
    myList = [5, 2, 7, 6, 9, 1]
    l = [e * 2 for e in myList if e % 2 == 0]
    print(l)
    print("==== Generator Expression =====")
    g1 = (num * 2 for num in range(5))
    print(g1)
    for e in g1:
        print(e)
    g2 = (e * 2 for e in myList if e % 2 == 0)
    print(g2)
    for e in g2:
        print(e)

if __name__ == "__main__":
    main()