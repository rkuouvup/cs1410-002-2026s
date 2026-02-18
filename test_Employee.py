from Employee import Employee
import math

def test_Employee_Default() -> None:
    e = Employee()
    assert e.name == "No Name"
    #assert e.salary == 0.0
    assert math.isclose(e.salary, 0.0)
def test_Employee_Provided() -> None:
    e = Employee("Amy", 90000.0)
    assert e.name == "Amy"
    assert math.isclose(e.salary, 90000.0)