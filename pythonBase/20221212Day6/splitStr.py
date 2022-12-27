str = 'wo-shi-chen-wei'
resultSplitV1 = str.split("-")
resultSplitV2 = str.split("-", maxsplit=2)

print(resultSplitV1)
print(resultSplitV2)

resultPartion = str.partition("-")
print(resultPartion)
# 返回 元组(分隔符左侧内容, 分隔符, 分隔符右侧内容)

resultRightPartion = str.rpartition("-")
print(resultRightPartion)
# 返回 元组(分隔符左侧内容, 分隔符, 分隔符右侧内容)

strAnother = "wo shi \n chen \r ha"
resultSplitLines = strAnother.splitlines()
print(resultSplitLines)