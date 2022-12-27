# 将所给列表的偶数索引对应的值 加10 然后生成新的列表

myList = [1, 3, 5, 7, 9]
resultList = []
for i in range(0, len(myList)):
    if i % 2 == 0:
        myList[i] += 10
print(myList)
