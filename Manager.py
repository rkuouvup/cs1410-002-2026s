from Employee import Employee

class Manager(Employee):
    def __init__(self):
        self._bonus = 0.0
        Employee._empCount += 1
    @property
    def bonus(self) -> float:
        return self._bonus
    @bonus.setter
    def bonus(self, value:float) -> None:
        self._bonus = value

def main() -> None:
    emp1 = Employee("Zara", 2000)
    mgr1 = Manager()
    print(f"emp1.salary: {emp1.salary}")
    mgr1.displayCount()
    mgr1.foo()

if __name__ == "__main__":
    main()