data = input("Please enter an integer: ")

try:
    x = int(data)
    inv = 1 / x
    print(f"The inverse of {x} is {inv}")
except (ValueError, ZeroDivisionError) as ex:
    print("Error:", type(ex).__name__, ex)
#except ValueError:
#    print("Not Valid!")
#except ZeroDivisionError:
#    print("Zero has no inverse")

print("==== End of program ====")