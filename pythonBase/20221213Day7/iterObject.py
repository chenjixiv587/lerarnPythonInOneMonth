from collections.abc import Iterable, Iterator

myList = [1, 2, 3]
# 判断是否是 可迭代对象
result = isinstance(myList, Iterable)
print(result)

iterList = iter(myList)
# 判断是否是迭代器
res = isinstance(iterList, Iterator)
print(res)

for i in iterList:
    print(i)
print("-------")
# 迭代器 不会迭代多次
for i in iterList:
    print(i)