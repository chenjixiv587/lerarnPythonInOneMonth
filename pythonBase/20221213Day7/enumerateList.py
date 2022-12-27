# 使用枚举来遍历 列表
myList = ['q', 'w', 'e', 'r']
result = enumerate(myList)
for inx, val in result:
    print(inx, val)