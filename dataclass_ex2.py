from dataclasses import dataclass, field
from typing import List

@dataclass
class Course:
    name: str
    capacity: int = 15
    students: List[str] = field(default_factory=list)

    def addStudent(self, std):
        self.students.append(std)

c1 = Course("Math", 30, ["Amy", "Betty"])
print(f"c1: {c1}")

c2 = Course("Science")
c2.addStudent("Cindy")
c2.addStudent("Daisy")
print(f"c2: {c2}")