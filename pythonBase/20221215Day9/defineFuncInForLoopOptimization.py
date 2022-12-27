def outer():
    funcList = []
    for i in range(1, 6):
        def inner(num):
            # 让函数立即执行i就会是每个循环的值了
            def immediatelyAction():
                print(num)
            return immediatelyAction
        funcList.append(inner(i))
    return funcList


outer()[0]()
outer()[1]()
# 1
# 2
