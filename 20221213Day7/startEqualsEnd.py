# 判断一个列表是否是 对称列表
# [1, 2, 3, 2, 1] 是对称列表
# [1, 2, 3, 4, 5] 不是对称列表

myList = [1, 2, 3, 4, 3, 2, 1]
newList = myList[::-1]
if myList == newList:
    print("对称列表")
else:
    print("不是对称列表")