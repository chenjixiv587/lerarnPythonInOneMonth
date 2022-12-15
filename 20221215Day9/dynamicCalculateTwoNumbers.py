def sumNums(a, b):
    return a + b


def plusNums(a, b):
    return a * b


def calculate(a, b, calculateFunc):
    """
    动态的对数据进行操作
    :param a:
    :param b:
    :param calculateFunc:  函数作为参数 而不是函数执行结果作为参数
    :return:
    """
    return calculateFunc(a, b)


print(calculate(1, 2, sumNums))
print(calculate(2, 3, plusNums))
