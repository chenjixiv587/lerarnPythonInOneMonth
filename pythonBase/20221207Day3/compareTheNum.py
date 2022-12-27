# 设定一个值 然后接受用户输入的值 并比较大小 直到猜到这个值

import random

computerNum = random.randint(50, 100)
while True:
    userNum = int(input("请输入一个整数: "))
    if userNum > computerNum:
        print("太大")
    elif userNum < computerNum:
        print("太小")
    else:
        print("恭喜你猜对了")
        break
