# 找出成绩第一名和最后一名学生的姓名
import random

info = [["q", 89], ["w", 23], ["E", 100], ["f", 67]]


# 以成绩位排序根据
def getScore(l):
    return l[1]


info.sort(key=getScore)
print(info[0][0], info[0][1])
print(info[-1][0], info[-1][1])


