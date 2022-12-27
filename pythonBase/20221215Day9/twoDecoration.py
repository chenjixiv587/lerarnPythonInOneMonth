def lines(func):
    def inner():
        print("-" * 30)
        func()

    return inner


def stars(func):
    def inner():
        print("*" * 30)
        func()

    return inner


# 再执行这个
@lines
# 先执行这个
@stars
def show():
    print("show me the code")


show()
