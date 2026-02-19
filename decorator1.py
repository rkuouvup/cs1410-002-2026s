def decorator(func):
    def wrapper():
        print("Before function call inside the decorator")
        func()
        print("After function call inside the decorator")
    return wrapper

def say_whee():
    print("Whee!")


print("before decoration")
say_whee()
print("after decoration")
say_whee = decorator(say_whee)
say_whee()