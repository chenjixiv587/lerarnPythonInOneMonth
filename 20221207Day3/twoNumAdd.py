# 接受用户输入的两个值 并且用户不发出停的指令 就不停
# 如果输入的值 有问题 就提示 并且开始重新输入

while True:

    num1 = float(input("请输入第一个数: "))
    num2 = float(input("请输入第二个数: "))
# 如果输入的有问题 就回头重新输入 这里就假设 两个数字其中一个  大于 100 就不行
    if num1 > 100 or num2 > 100:
        print("您给的数据不合格，请重新输入")
        continue
    result = num1 + num2
    print(result)
# 询问用户是否要退出
    isQuit = input("按 q 退出计算，按其他键继续计算").lower()
    if isQuit == 'q':
        break

