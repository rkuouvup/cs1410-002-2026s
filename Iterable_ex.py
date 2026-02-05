from typing import Iterable, Iterator
from iterator_ex import SequenceIterator

class MyIterable:
    def __init__(self, sequence:Iterable) -> None:
        self._sequence = sequence
    def __iter__(self) -> Iterator:
        return SequenceIterator(self._sequence)

def main() -> None:
    l = [1, 2, 3, 4]
    for e in l:
        print(e)
    print("==========")
    s = MyIterable(l)
    #print(next(s))
    for e in s:
        print(e)

    print("==========")
    myiter = iter(s)
    while True:
        try:
            print(next(myiter))
        except StopIteration:
            break
    print("============")
    l = [1, 2, 3, 4]
    newList = []
    for e in l:
        newList.append(e * 2)
    print(newList)
    print("============")
    compList = [e * 2 for e in l]
    print(compList)
    print("============")
    sList = [e * 2 for e in s]
    print(sList)


if __name__ == "__main__":
    main()