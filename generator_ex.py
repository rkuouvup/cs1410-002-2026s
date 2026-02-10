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

if __name__ == "__main__":
    main()