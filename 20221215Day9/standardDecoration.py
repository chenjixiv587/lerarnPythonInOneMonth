def lines(func):
    def inner(*args, **kwargs):
        print("-" * 30)
        res = func(*args, **kwargs)
        return res
    return inner


def stars(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)

    return inner


@lines
def show(num1, num2, num3):
    print(num1, num2, num3)
    return num1 + num2 + num3


show(1, 2, num3=3)
