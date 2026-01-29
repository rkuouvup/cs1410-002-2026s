"""
Ambiguity Problem
"""
class LeftSubclass():
    num_left_calls = 0
    def call_me(self) -> None:
        print("Calling method on LeftSubclass")
        self.num_left_calls += 1

class RightSubclass():
    num_right_calls = 0
    def call_me(self) -> None:
        print("Calling method on RightSubclass")
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def foo(self):
        print("foo")
    def call_me(self) -> None:
        RightSubclass.call_me(self)

def main() -> None:
    s = Subclass()
    s.foo()
    s.call_me()

if __name__ == "__main__":
    main()