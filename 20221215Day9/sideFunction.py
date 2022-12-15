import functools


def total(a, b=1):
    return a + b


newFun = functools.partial(total, b=2)
print(newFun(2))
