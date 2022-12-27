# 用户指定一个数字 求这个数字的阶乘

userNum = input("Please give a number: ")
userNum = int(userNum)

num = 0
result = 1
while num < userNum:
    num += 1
    result *= num
print(result)
