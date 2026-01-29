class Adder():
    def add(self, x, y):
        ...
class IntAdder(Adder):
    def add(self, x:int, y:int) -> int:
        print("IntAdder")
        return x + y
class FloatAdder(Adder):
    def add(self, x:float, y:float) -> float:
        print("FloatAdder")
        return x + y
"""class AccountAdder(Adder):
    def add(self, x:Account, y:Account):
        return x.balance + y.balace"""

def add(adder:Adder) -> None:
    print(adder.add(2, 3))

iadder = IntAdder()
fadder = FloatAdder()
add(iadder)
add(fadder)