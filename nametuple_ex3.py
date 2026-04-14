from collections import namedtuple

#namedtuple("StuColl", "name age marks")
StuColl = namedtuple("StuColl", ["name", "age", "marks"])
def calculate_average_grade(std):
    total_marks = sum(std.marks)
    avg_grade = total_marks / len(std.marks)
    return avg_grade

sc1 = StuColl(name="Ain Ruth", age=22, marks=[89, 92, 75, 90, 86])
print(sc1)
avgerage_grade = calculate_average_grade(sc1)
print(f"Average Grade: {avgerage_grade}")

print("==================")

from typing import NamedTuple

class StuTyping(NamedTuple):
    name: str
    age: int
    marks: list

    def calculate_average_grade(self):
        total_marks = sum(self.marks)
        avg_grade = total_marks / len(self.marks)
        return avg_grade


st1 = StuTyping(name="Ain Ruth", age=22, marks=[89, 92, 75, 90, 86])
print(st1)
print(f"average grade: {st1.calculate_average_grade()}")
st1.age = 23