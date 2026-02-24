def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call inside the decorator")
        func(*args, **kwargs)
        print("After function call inside the decorator")
    return wrapper

def say_words(words):
    print(words)

def foo(a, b, c, d):
    print(a, b, c, d)


print("====== before decoration ======")
say_words("Hello")
foo(1, 2, 3, 4)
print("====== after decoration =======")
say_words = decorator(say_words)
say_words("Whee!")
foo = decorator(foo)
foo(1, 2, 3, 4)