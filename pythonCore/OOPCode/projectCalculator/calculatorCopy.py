# 实现一个计算器

class Calculator:
    # 验证输入数据的可靠性
    def __check(func):
        def inner(self, n):
            if not isinstance(n, int):
                raise ValueError("不是整数")
            return func(self, n)

        return inner

    @__check
    def __init__(self, startNum):
        self.__result = startNum

    @__check
    def jia(self, n):
        self.__result += n
        return self

    @__check
    def jian(self, n):
        self.__result += n
        return self

    @__check
    def cheng(self, n):
        self.__result *= n
        return self

    @__check
    def chu(self, n):
        pass

    def clear(self):
        self.__result = 0
        return self

    def show(self):
        print(self.__result)

    @property
    def result(self):
        return self.__result


c1 = Calculator(100).jia(100).jian(89)
print(c1.result)
