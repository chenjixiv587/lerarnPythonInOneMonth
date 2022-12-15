def sumNum(*args):
    total = 0
    # print(args)  元组
    for i in args:
        total += i
    return total


print(sumNum(1, 2, 3))
