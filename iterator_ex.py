from typing import Iterable, Iterator#, Any

class SequenceIterator:
    def __init__(self, sequence:Iterable) -> None:
        self._sequence:Iterable = sequence
        self._index:int = 0
    def __iter__(self) -> Iterator:
        return self
    def __next__(self) -> int | float:#-> Any:
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item * item
        else:
            raise StopIteration


def main() -> None:
    # Repeat the code
    print("Hello")
    print("Hello")
    print("Hello")

    # Using iteration structure
    print("===== Using the iteration structure =====")
    times = 0
    while times < 3:
        print("Hello")
        times += 1

    # Iterate throught a container/a stream of data
    numbers = [1, 2, 3, 4]
    for number in numbers:
        print(number)

    # List is not an iterator but an iterable
    #print(next(numbers))

    # Use user defined iterator object
    s = SequenceIterator(numbers)
    for i in range(3):
        print(next(s))
    print("================")   
    for e in SequenceIterator(numbers):
         print(e)

if __name__ == "__main__":
    main()