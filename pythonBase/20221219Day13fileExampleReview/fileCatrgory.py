# 20221220 made by brucechen
# 需求
#     对文件夹中的文件依据文件的后缀名进行分类 把分类结果保存在一个 result.txt 文件中
#
# 思路
#     判断被操作的文件夹是否存在
#     定位到需要操作的文件夹
#     遍历整个文件夹 得到文件
#     获得文件的后缀名
#         判定是否存在这样的文件夹
#             如果没有则新建 然后将文件移到文件夹中
#             如果有 直接将文件移到文件中
#
#
#     遍历整个文件夹
#         判断获取的是文件夹还是文件
#             是文件夹 则继续遍历 判断 这里就是递归  要用函数
#             是文件 就写入到目标txt 中
#
#
import os
import shutil

filePath = "files"
if not os.path.exists(filePath):
    print("路径不正确，请重新选择路径")
    exit()
os.chdir(filePath)
filesNeedMove = os.listdir("/")


def moveFiles(files):
    for file in files:
        indexOfExtension = file.rfind(".")
        if indexOfExtension == -1:
            continue
        extension = file[indexOfExtension + 1:]
        if extension not in files:
            os.mkdir(extension)
        shutil.move(file, extension)

moveFiles(filesNeedMove)

os.chdir("../../")
def resultToTxt(files, resultTxt):
    filesList = os.listdir(files)
    for file in filesList:
        newDir = files + "/" + file
        if os.path.isdir(newDir):
            resultTxt.write(newDir + "\n")
            resultToTxt(newDir, resultTxt)
        else:
            resultTxt.write("\t" + file)
    resultTxt.write("\n")

with open("result.txt", "a") as toTxt:
    resultToTxt("files", toTxt)
