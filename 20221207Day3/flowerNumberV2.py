# 判断一个三位数是否是水仙花数
# 判断是否是个 三位数
# 判断 百位的三次方 + 十位的三次方 + 个位的三次方 = 本身

# 判断用户输入的是否是 三位数
flag = True
while flag:
    userNum = input("请输入一个三位数: ")
    userNum = int(userNum)
    # 判断是否是 三位数
    if not (99 < userNum < 1000):
        print("不是三位数，请重新输入")
        continue

    # 取得百位
    hundredNum = userNum // 100
    # print(hundredNum)
    # 取得十位
    tenNum = userNum // 10 % 10
    # print(tenNum)
    # 取得个位
    lastNum = userNum % 10
    # print(lastNum)
    # 判断是否是 水仙花数
    sumThree = hundredNum ** 3 + tenNum ** 3 + lastNum ** 3
    if sumThree == userNum:
        print("恭喜你这个数是水仙花数")
        break
    else:
        print("Sorry 你这个数不是水仙花数, 再试试别的数字看看")

