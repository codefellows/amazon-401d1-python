# what is the scope here?

spam = "spam as text"

print("outside func", spam)


def some_func():
    global spam

    print(f"inside some_func spam {spam}")
    spam = "spam from inside function"
    eggs = "eggs string"
    print(f"inside some_func eggs {eggs} and {spam}")
    return eggs


return_val = some_func()

print(f"outside {return_val}")

# print(f"outside {eggs}")

print("some stuff {} and {}".format("sock","cup"))


