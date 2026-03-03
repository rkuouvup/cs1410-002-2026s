from typing import Final, Any
from enum import Enum, auto

class Suit(Enum):
    Heart = auto()
    Diamond = auto()
    Club = 40
    Spade = auto()

class Month(Enum):
    Jan = auto()
    Feb = auto()

class Day(Enum):
    Monday = auto()
    Tuesday = auto()
    Wednesday = auto()
    Thursday = auto()
    Friday = auto()
    Saturday = auto()
    Sunday = auto()

    def get_abbr(self) -> str:
        return self.name[:3]
    @classmethod
    def first_day_cal(cls) -> str:
        return cls.Sunday.name

class Direction(Enum):
    @staticmethod
    def _generate_next_value_(name:str, start:int, count:int, last_values:list[Any]) -> Any:
        return name[0]
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


def main() -> None:
    # If there is no enumeration in the language
    # Define the constants in all upper cases variables
    HEART:Final[int] = 1
    DIAMOND:Final[int] = 2
    CLUB:Final[int] = 3
    SPADE:Final[int] = 4

    card1 = (DIAMOND, 5)
    card2 = (SPADE, 9)

    print(f"Compare card 1 and card2:")
    if (card1[0] == card2[0] and card1[1] == card2[1]):
        print(f"The two cards are the same")
    else:
        print(f"The two cards are different")

    JAN:Final[int] = 1
    FEB:Final[int] = 2
    date1 = (FEB, 5)

    print(f"Compare card1 and date1: ")
    if (card1[0] == date1[0] and card1[1] == date1[1]):
        print(f"The two elements are the same")
    else:
        print(f"The two elements are different")

    print("=========================")
    # Using Enumeration Class
    # What constants are defined in the enumerations
    print(f"Suit Enumeration: {Suit}")
    print(f"Suit Enumeration: {list(Suit)}")
    print(f"Month Enumeration: {list(Month)}")

    print(f"Compare Suit.Diamond and Month.Feb: {Suit.Diamond == Month.Feb}")

    # Extend enumeration with new behavior
    day1 = Day.Monday
    print(f"The abbrivation of day1 is {day1.get_abbr()}")
    print(f"The first day of the week: {Day.first_day_cal()}")

    print("=================")
    # Tweak default behavior of auto() method
    print(f"Enumeration of Direction: {list(Direction)}")

    

if __name__ == "__main__":
    main()