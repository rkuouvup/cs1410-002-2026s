"""
Example of return a function as an object
"""
def parent(num):
    def first_child():
        return "Amy"
    def second_child():
        return "Betty"
    if num == 1:
        return first_child
    else:
        return second_child

"""
Example of pass a function as an object to another function
"""
def say_hello(name):
    return f"Hello {name}"
def be_awesome(name):
    return f"{name}, you are awesome!" 

def greeting(f, name):
    print(f(name))

def main() -> None:
    first = parent(1)
    print(first)
    first_call = first()
    print(first_call)

    greeting(say_hello, "Amy")
    greeting(be_awesome, "Betty")

if __name__ == "__main__":
    main()