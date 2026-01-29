class Employee:
    _empCount:int = 0
    def __init__(self, name:str = "No Name", salary:float = 0.0):
        self._name:str = name
        self._salary:float = salary
        Employee._empCount += 1

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value:str) -> None:
        self._name = value
    @property
    def salary(self) -> float:
        return self._salary
    @salary.setter
    def salary(self, value:float) -> None:
        self._salary - value
    def displayEmployee(self) -> None:
        print(f"Name: {self._name}, Salary: {self._salary}")
    def displayCount(self):
        print(f"Total Employee: {Employee._empCount}")
    def foo(self) -> None:
        print("Example of Inheritance")

def main() -> None:
    emp1 = Employee("Zara", 2000)
    emp2 = Employee("Manni", 5000)
    emp1.displayEmployee()
    print(f"Employee 2 (name: {emp2.name}, salary: {emp2.salary})")

    emp1.displayCount()

if __name__ == "__main__":
    main()