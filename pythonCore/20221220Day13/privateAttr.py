# 私有化

class Person:
    def __init__(self):
        self.__age = 10

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if isinstance(age, int) and 0 < age < 100:
            self.__age = age
        else:
            print("age is wrong")


p = Person()
p.setAge(90)
print(p.getAge())
