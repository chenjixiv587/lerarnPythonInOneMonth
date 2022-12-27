l = (i for i in range(0, 100) if i % 2 == 0)
print(next(l))
print(l.__next__())
