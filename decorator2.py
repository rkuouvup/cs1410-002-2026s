def decorator(func, words):
    def wrapper():
        print("Before function call inside the decorator")
        func(words)
        print("After function call inside the decorator")
    return wrapper

def say_words(words):
    print(words)


print("====== before decoration ======")
say_words("Hello")
say_words("Whee!")
print("====== after decoration =======")
say_words = decorator(say_words, "Whee!")
say_words()