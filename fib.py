from typing import Iterator
def fib(n:int) -> int:
    """ recursive style
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    """
    current:int = 0
    next:int = 1

    if n < 0:
        raise ValueError
    elif n == 0:
        return current
    elif n == 1:
        return next
    else:
        for i in range(1, n):
            fib_num:int = current + next
            current = next
            next = fib_num
        return fib_num

class FibIterator:
    def __init__(self, stop:int) -> None:
        if stop < 0:
            self._stop:int = 0
        else:
            self._stop:int = stop
        self._index:int = 0
        self._current:int = 0
        self._next:int = 1
    def __iter__(self) -> Iterator:
        return self
    def __next__(self) -> int:
        if self._index <= self._stop:
            """
            data:int = self._index
            self._index += 1
            return data"""
            fib_number:int = self._current
            """self._current = self._next
            self._next = fib_number + self._next"""
            self._current, self._next = (self._next, self._current + self._next)
            self._index += 1
            return fib_number
        else:
            raise StopIteration
            


def main() -> None:
    print(fib(5)) # 5
    print(fib(7)) # 13
    for fibNumber in FibIterator(5):
        print(fibNumber)  # 0, 1, 1, 2, 3, 5

if __name__ == "__main__":
    main()