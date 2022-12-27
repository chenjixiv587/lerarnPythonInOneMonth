class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "小狗的名字是:{0}, 小狗的年龄是:{1}".format(self.name, self.age)

    def __repr__(self):
        return "地址信息"


p = Person("david", 11)
s = str(p)
print(p)
print(repr(p))


## __call__ ##

class PenFactory:
    def __init__(self, penType):
        self.penType = penType

    def __call__(self, penColor):
        print("创建一个{0},色彩是{1}".format(self.penType, penColor))


pencil = PenFactory("pencil")
pencil("red")

ballPen = PenFactory("ballPen")
ballPen("black")


## 索引操作

class Dog:
    def __init__(self):
        self.cache = {}

    def __setitem__(self, key, value):
        self.cache[key] = value

    def __getitem__(self, item):
        return self.cache[item]

    def __delitem__(self, key):
        del self.cache[key]


dog = Dog()
dog["name"] = "snoopy"
print(dog["name"])
del dog["name"]
print(dog.cache)


# 切片操作-------------------
class Cat:
    def __init__(self):
        self.cache = [1, 2, 3, 4, 5]

    def __setitem__(self, key, value):
        self.cache[key] = value

    def __getitem__(self, item):
        return self.cache[item]

    def __delitem__(self, key):
        del self.cache[key]


cat = Cat()
cat[0: 4: 2] = ("a", "b")
print(cat.cache)


# 比较 -- -- -- 就相当于是  自定义
class School:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.width == other.width

    def __ne__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __le__(self, other):
        pass


# ----遍历--
# 方式1
class Home:
    def __init__(self):
        self.result = 1

    def __getitem__(self, item):
        self.result += 1
        if self.result >= 6:
            raise StopIteration("stop")
        return self.result


h = Home()
for i in h:
    print(i)


# ----遍历--
# 方式2
class Home2:
    def __init__(self):
        self.result = 1

    def __getitem__(self, item):
        self.result += 1
        if self.result >= 6:
            raise StopIteration("stop")
        return self.result

    # 优先级高
    # 如果只有__iter__ 那么就必须返回iter()处理过的数据
    # 如果没有处理 那么必须要有__next__()
    def __iter__(self):
        # return iter([1, 3, 5, 6])
        return self

    def __next__(self):
        self.result += 1
        if self.result >= 6:
            raise StopIteration("stop")
        return self.result



# 如果只需要用 next() 方法 那么就只需要自定义 __next__ 而不需要 __iter__
# next(h2)
h2 = Home2()
for j in h2:
    print(j)
