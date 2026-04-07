"""
    List Sorting
"""

toys = ['bicycle', 'train', 'doll', 'teddy bear',
        'kite', 'ball', 'video game set']

print(f"toys: {toys}")
#toys.sort(reverse=True)
toys.sort(key=len)

def lastLetter(e):
    return e[-1]

toys.sort(key=lastLetter)

from operator import itemgetter

toys.sort(key=itemgetter(1))
print(f"toys: {toys}")

print("===========================")

"""
    Tuple Sorting
"""

toys = ('bicycle', 'train', 'doll', 'teddy bear',
        'kite', 'ball', 'video game set')
print(f"toys: {toys}")

toys_sorted = sorted(toys)

def thirdLetter(e):
    return e[2]
toys_sorted = sorted(toys, key=thirdLetter)

toys_sorted = sorted(toys, key=itemgetter(3), reverse=True)

print(f"toys: {toys}")
print(f"toys_sorted: {toys_sorted}")

print("===========================")

"""
    Dictionary Sorting
"""

d = {'watermelon': 1, 'apple': 2, 'banana': 3}
print(f"d: {d}")

#for e in d:
#    print(e)

d_sorted = dict(sorted(d.items()))
print(f"d_sorted: {d_sorted}")

print("===========================")

"""
    List of Dictionary Sorting
"""

emp_dict = [{'name': 'Daisy', 'age': 54, 'salary': 67000},
            {'name': 'Amy', 'age': 38, 'salary': 45000},
            {'name': 'Cindy', 'age': 23, 'salary': 76000}]
print(f"emp_dict: {emp_dict}")
#emp_dict.sort()

def emp_age(e):
    return e['age']

emp_dict_sorted = sorted(emp_dict, key=emp_age)
emp_dict_sorted = sorted(emp_dict, key=itemgetter('name'))
print(f"emp_dict_sorted: {emp_dict_sorted}")

print("===========================")

"""
    List of Dictionary Sorting
"""

class Employee:
    def __init__(self, name:str, age:int, salary:float) -> None:
        self.name:str = name
        self.age:int = age
        self.salary:float = salary
    def __repr__(self) -> str:
        return self.name + " (age: " + str(self.age) + \
               ", salary: " + str(self.salary) + ")"
    
emp = [Employee('Daisy', 54, 67000),
       Employee('Amy', 38, 45000),
       Employee('Cindy', 23, 76000)]

print(f"emp: {emp}")

def emp_obj_age(e):
    return e.age

emp_sorted = sorted(emp, key=emp_obj_age)
# lambda parameter: return_value
emp_sorted = sorted(emp, key=lambda e: e.salary)

from operator import attrgetter

emp_sorted = sorted(emp, key=attrgetter('name'))
print(f"emp_sorted: {emp_sorted}")