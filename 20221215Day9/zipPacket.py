def show(a, b):
    return a + b


def test(**args):
    # 拆包
    print(args)
    # 装包
    print(show(**args))


test(a=2, b=7)
