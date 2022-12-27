import sys

class Person:
    pass

# sys.getrefcount(p1) 也是一种引用 会加1 真正记数的时候需要  -1
p1 = Person()
print(sys.getrefcount(p1))

p2 = p1
print(sys.getrefcount(p1))
del p2
print(sys.getrefcount(p1))

