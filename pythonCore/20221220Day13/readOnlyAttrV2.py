# 只读属性
# 先隐藏 再部分公开
class Person(object):
    def __init__(self):
        self.__age = 10

    @property
    def age(self):
        return self.__age

print(Person().age)
# Person().age = 100  # 不给设置
