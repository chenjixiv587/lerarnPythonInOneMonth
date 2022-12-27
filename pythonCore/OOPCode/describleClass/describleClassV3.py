class Age:
    def __get__(self, instance, owner):
        print("get")

    def __set__(self, instance, value):
        print("set")

    def __delete__(self, instance):
        print("delete")


class Person:
    age = Age()

    def __init__(self):
        self.__age = 10


p = Person()
print(p.age)
# 这种情况下 每个新建出来的实列都会共用这个age 所以不会私人订制  这样就很不好