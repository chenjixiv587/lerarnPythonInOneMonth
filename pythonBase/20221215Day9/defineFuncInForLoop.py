def outer():
    funcList = []
    for i in range(1, 6):
        def inner():
            print(i)

        funcList.append(inner)
    return funcList


outer()[0]()
outer()[1]()
# 5
# 5
#  为什么都是 5 呢  因为在定义 inner() 函数的时候 并不是执行 所以 i  并不能确定
#  等最后 执行的时候  i  已经变成了 5
