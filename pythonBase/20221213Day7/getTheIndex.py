# [1, 2, 3, 4, 2, 5, 7, 2]
# 取得 2 所有的索引
# 取得 2 的个数

myList = [1, 2, 3, 4, 2, 5, 7, 2]
count = 0
# myList.index()
for i in range(0, len(myList)):
    if myList[i] == 2:
        count += 1
        print(i)
print(count)

countTwo = myList.count(2)
print(countTwo)

