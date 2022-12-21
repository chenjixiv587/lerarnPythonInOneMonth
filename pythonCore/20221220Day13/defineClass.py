class Person:
    # 限定由类产生的对象所拥有的属性
    __slots__ = ["age", "sex"]
    pass

bruce = Person()
bruce.num = 1


