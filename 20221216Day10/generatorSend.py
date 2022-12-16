def test():
    print("start")
    res1 = yield 1
    print(res1)

    res2 = yield 2
    print(res2)


t = test()
# 执行过程 就是 到 yield 1 进行挂起  然后 1 传给 t.__next__()
# 此时 1 还没有给 res1
# print(t.__next__())
# start
# 1


# 执行过程 就是 到 yield 2 进行挂起  然后 1 传给 t.__next__()
# 此时 res1 = None
# print(t.__next__())
# None
# 2


# 用 send() 改善
t.send(None)
t.send("999")

