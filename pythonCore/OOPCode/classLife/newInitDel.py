# 需求  在创建实列的时候  告知客户 有多少个实列

# 切记  self  指向的是  创建的 实例
class Person:
    __personCount = 0

    def __init__(self):
        # print("创建+1")
        Person.__personCount += 1

    def __del__(self):
        # print("减少一个")
        Person.__personCount -= 1

    @classmethod
    def log(cls):
        print("{0}".format(cls.__personCount))


p1 = Person()
p2 = Person()
Person.log()
