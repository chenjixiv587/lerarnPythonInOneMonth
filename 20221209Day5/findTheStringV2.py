# 接受用户输入一个字符串和一个字符串，然后判断字符串是否存在，如果存在并给出这个字符的所有位置

originStr = input("请输入一个字符串: ")
findStr = input("请输入你要查找的字符串: ")

result = -1
while True:
    result = originStr.find(findStr, result+1)
    if result == -1:
        break
    else:
        print(result)

