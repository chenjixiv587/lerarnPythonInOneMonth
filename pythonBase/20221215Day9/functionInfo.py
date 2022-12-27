def test(a, b = 20):
    """
    用于计算 两个数的 和 和 积
    :param a: 数值类型  不可省略 没有默认值
    :param b: 数值类型 可省略 默认 是 20
    :return:  返回一个 元组  (和,积)
    """
    sumNum = a + b
    plusNum = a * b
    return (sumNum, plusNum)

print(test(10))

help(test)