def odd():
    print("偶数")
    yield 2
    print("ss")
    yield 4


l = odd()
print(next(l))  # 到 yield 2 打断 并记录位置
print(next(l))
