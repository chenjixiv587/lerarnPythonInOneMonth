# 描述器 第一个版本

class Person:
    def __init__(self):
        self.__age = 90

    def setAge(self, value):
        self.__age = value

    def getAge(self):
        return self.__age

    def delAge(self):
        del self.__age

    age = property(getAge, setAge, delAge)


p = Person()
print(p.age)
p.age = 1000
print(p.age)
print(p.__dict__)