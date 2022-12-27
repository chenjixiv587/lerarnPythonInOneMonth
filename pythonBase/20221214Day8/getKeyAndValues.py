myDic = {
    "name": "chen",
    "age": 12
}
newDic = {}
for k, v in myDic.items():
    newK, newV = v, k
    newDic[newK] = newV
myDic = newDic
print(newDic)
print(myDic)

