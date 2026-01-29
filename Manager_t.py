from Employee import Employee

class Manager(Employee):
    def __init__(self, name:str="No Name", salary:float=0.0, bonus:float = 0) -> None:
        super().__init__(name, salary)
        self._bonus:float = bonus
        Employee._empCount += 1
    @property
    def bonus(self) -> float:
        return self._bonus
    @bonus.setter
    def bonus(self, value: float) -> None:
        self._bonus = value
    def displayEmployee(self) -> None:
        print(f"Name: {self._name}, Salary: {self._salary + self._bonus}")


def main() -> None:
    emp1 = Employee("Zara", 2000)
    mgr1 = Manager("Manni", 5000, 1000)
    print(f"emp1.salary: {emp1.salary}")
    mgr1.displayCount()
    mgr1.foo()

    emp1.displayEmployee()
    mgr1.displayEmployee()

if __name__ == "__main__":
    main()
