# 只读属性
# 先隐藏 再部分公开
class Person:
    def __init__(self):
        self.__age = 10

    def getAge(self):
        return self.__age


print(Person().getAge())
