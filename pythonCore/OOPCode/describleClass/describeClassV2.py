class Person:
    def __init__(self):
        self.__age = 19

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >100 or value < 0:
            raise ValueError("年龄不对")
        self.__age = value

    @age.deleter
    def age(self):
        del self.__age


p = Person()
print(p.age)
p.age = 10
print(p.age)
del p.age
print(p.age)