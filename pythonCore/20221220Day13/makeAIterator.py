from collections.abc import Iterator


class Person:
    def __init__(self):
        self.age = 1

    # 迭代器的话  必须  __iter__ __next__ 同时满足
    def __iter__(self):
        # self.age = 1 添加这个语句 那么迭代器就可以复用
        # self.age = 1
        return self

    def __next__(self):
        self.age += 1
        if self.age >= 6:
            raise StopIteration("stop")
        return self.age


p = Person()
print(isinstance(p, Iterator))
for i in p:
    print(i)
