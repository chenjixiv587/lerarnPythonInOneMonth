class Age:
    def __get__(self, instance, owner):
        return instance.v

    def __set__(self, instance, value):
        instance.v = value

    def __delete__(self, instance):
        del instance.age


class Person:
    age = Age()


p1 = Person()
p1.age = 100
print(p1.age)

p2 = Person()
p2.age = 1
print(p2.age)