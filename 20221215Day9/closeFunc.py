def outer(anotherArgument):
    outerArgument = 99

    def inner():
        return outerArgument + anotherArgument

    return inner


print(outer(100)())
