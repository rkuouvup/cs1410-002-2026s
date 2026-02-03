from __future__ import annotations

class TimeHourMinute:
    def __init__(self, hour:int = 0, minute:int = 0) -> None:
        carry:int = minute // 60
        self._minute:int = minute % 60
        self._hour:int = hour + carry

    def __repr__(self) -> str:
        return f"{self._hour}:{self._minute}"
    
    def setTime(self, hour:int, minute:int) -> None:
        self.__init__(hour, minute)
    
    def __add__(self, value:int|TimeHourMinute) -> TimeHourMinute:
        if isinstance(value, TimeHourMinute):
            return TimeHourMinute(self._hour + value._hour, self._minute + value._minute)
        elif isinstance(value, int):
            return TimeHourMinute(self._hour + value, self._minute)
        else:
            raise TypeError("Incorrect type")
        
    def __radd__(self, value:int|TimeHourMinute) -> TimeHourMinute:
        if isinstance(value, TimeHourMinute):
            return TimeHourMinute(self._hour + value._hour, self._minute + value._minute)
        elif isinstance(value, int):
            return TimeHourMinute(self._hour + value, self._minute)
        else:
            raise TypeError("Incorrect type")
        
    def _iadd__(self, value:int|TimeHourMinute) -> TimeHourMinute:
        if isinstance(value, TimeHourMinute):
            hr = self._hour + value._hour
            min = self._minute + value._minute
        elif isinstance(value, int):
            hr = self._hour + value
            min = self._minute
        else:
            raise TypeError("Incorrect type")
        self.setTime(hr, min)
        return self

def main() -> None:
    t1 = TimeHourMinute(1, 100)
    print(t1)
    t2 = t1 + 3
    t3 = 5 + t1
    print(t2)
    print(t3)
    print(t1 + t2)
    t1 += t2
    print(t1)
    t1 += 5
    print(t1)

if __name__ == "__main__":
    main()