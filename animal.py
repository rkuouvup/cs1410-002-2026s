from abc import ABC, abstractmethod
from typing import override

class Animal(ABC):
    def __init__(self, name:str = "No Name") -> None:
        self.name = name
    @abstractmethod
    def make_sound(self) -> str:
        pass
    @property
    @abstractmethod
    def species(self) -> str:
        pass

class Dog(Animal):
    @override
    def make_sound(self) -> str:
        return "Bark"
    @property
    def species(self) -> str:
        return "Canine"

class Cat(Animal):
    @override
    def make_sound(self) -> str:
        return "Miao"
    
    #def make_sound(self, )
    
    @property
    def species(self) -> str:
        return "Feline"



def DisplayAnimal(animal: Animal):
    print(f"{animal.name}: {animal.species}")

def MakeSound(animal:Animal) -> None:
    print(f"{animal.name}: {animal.make_sound()}")

def main() -> None:
    d = Dog("Hana")
    c = Cat("Momo")
    DisplayAnimal(d)
    DisplayAnimal(c)
    MakeSound(d)
    MakeSound(c)

if __name__ == "__main__":
    main()