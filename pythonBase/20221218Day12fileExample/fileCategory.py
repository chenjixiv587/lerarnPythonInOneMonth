# 　文件操作　一定要注意路径　路径　　路径　
# 需求 将文件夹中的文件 分门别类放在以文件后缀名为名字的文件夹中
# 将文件的摆放结果放在一个txt文件里

# 1 将目录切换到需要操作的文件目录
import os
import shutil

# print(os.getcwd())
filePath = "filesss"
if not os.path.exists(filePath):
    print("路径不存在，请重新确认")
    exit()
os.chdir(filePath)
# 2 遍历整个文件夹
files = os.listdir("/")
for file in files:
    # 3 提取出文件的后缀名
    index = file.rfind(".")
    if index == -1:
        continue
    extension = file[index + 1:]
    # 4 如果文件夹中有后缀名的目录 那么就将文件放在文件夹里
    if extension not in files:
        os.mkdir(extension)
    # 5 如果没有 则新建文件夹  并把文件放在文件夹里
    shutil.move(file, extension)
# 6 将结果写在一个 .txt 文件里
# 通过一个函数来实现
os.chdir("../../")


def listFileToTxt(dirName, toFile):
    # 想要获得文件夹的明细 就得遍历整个文件夹
    fileList = os.listdir(dirName)
    for fileName in fileList:
        # 如果遍历出来还是个文件夹就得继续遍历得到的文件夹 就是递归
        # 　注意传入的是路径
        newDir = dirName + "/" + fileName
        if os.path.isdir(newDir):
            # print(newDir)
            toFile.write(newDir + "\n")
            listFileToTxt(newDir, toFile)
            # 如果遍历出来的是文件就打印
        else:
            # print("\t" + fileName)
            toFile.write("\t" + fileName + "\n")
    # print()
    toFile.write("\n")


with open("result.txt", "a") as f:
    listFileToTxt(filePath, f)
