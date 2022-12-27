# 随机生成一个 10 位列表  列表的每个元素是  10 -20 之间的整数
import random
myList = []
for n in range(0, 10):
    num = random.randint(10, 20)
    myList.append(num)
print(myList)
