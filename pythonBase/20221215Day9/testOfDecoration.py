def changeType(char):
    def typeIt(func):
        def inner(*args, **kwargs):
            print(char * 30)
            res = func(*args, **kwargs)
            return res
        return inner

    return typeIt


@changeType("-")
def show(num1, num2, num3):
    print(num1, num2, num3)
    return num1 + num2 + num3


print(show(1, 2, num3=3))
