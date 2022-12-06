# 获得身高体重性别年龄 计算出体脂率 然后告知是否在合理的范围内
print("您好，欢迎进入体脂率计算平台!")
# 获得身高 体重 年龄 性别
height = int(input("请输入您的身高(单位为cm): ")) / 100
weight = int(input("请输入您的体重(单位为kg): "))
age = int(input("请输入您的年龄: "))
gender = input("请输入您的性别(男/女): ")
# 数据容错处理
if not (0 <= height <= 3 and 0 <= weight <= 100 and 0 <= age <= 90 and (gender == 0 or gender == 1)):
    print("数据有问题，程序退出")
    exit()

# 计算体脂率
if gender == "男":
    genderNum = 1
else:
    genderNum = 0

# 1）BMI=体重（公斤）÷（身高×身高）（米）；
bmi = weight / (height * height)
# （2）体脂率：1.2×BMI+0.23×年龄-5.4-10.8×性别（男为1，女为0）。
body = 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * genderNum
# 与标准比较
# 男性体脂率 15 %- 18 % 女性 25% - 28%

if genderNum == 1:
    if 15 <= body <= 18:
        print("您好，男士，合格")
    else:
        print("您好，男士，不合格")
else:
    if 25 <= body <= 28:
        print("您好，女士，合格")
    else:
        print("您好，女士，不合格")

# 在没有判断语句时候 这个是个技巧
# minBody = 15 + 10 * (1 - genderNum)
# maxBody = 18 + 10 * (1 - genderNum)

# # 告知
# print(minBody <= body <= maxBody)
