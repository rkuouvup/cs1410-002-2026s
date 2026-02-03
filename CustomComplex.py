from __future__ import annotations

class CustomComplex:
    def __init__(self, real:int|float, imag:int|float) -> None:
        self._real:int|float = real
        self._imag:int|float = imag
    def __add__(self, other:int|float|CustomComplex) -> CustomComplex:
        if isinstance(other, int) or isinstance(other, float):
            result = CustomComplex(self._real + other, self._imag)
                        #.        int     +  CustomComplex
        elif isinstance(other, CustomComplex):
            result = CustomComplex(self._real + other._real,
                                   self._imag + other._imag)
        else:
            raise TypeError
        return result
    def __str__(self) -> str:
        return f"{self._real}+{self._imag}j"
    
def main()->None:
    c1 = CustomComplex(1, 2)
    c2 = CustomComplex(3, -4)
    print(f"c1 + 1.5: {c1 + 1}")
    print(f"c1 + c2: {c1 + c2}")
if __name__ == "__main__":
    main()