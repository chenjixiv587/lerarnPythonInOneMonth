myDic = {
    "name": "chen",
    "age": 12
}

# del myDic
# print(myDic)
# pop 返回key 所对应的 值  如果 Key 不存在 而且给了默认值 那么就返回默认值 没有 就报错
# print(myDic.pop("name"))
# print(myDic.pop("gender", "man"))
# print(myDic)

# popitem()  返回被删除的元素组成的 元组
# print(myDic.popitem())
# print(myDic)

myDic.clear()
print(myDic)