# 随机生成一个8 位列表 列表元素是 1- 10 之间随机整数 生成好之后 再进行降序排序

from random import randint
randomList = []
for i in range(0, 8):
    randomList.append(randint(1, 10))
reversedList = sorted(randomList, reverse=True)
print(reversedList)
