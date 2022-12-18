# 文件的分类摆放
"""
需求
有 .txt .avi .pdf 等等的文件  将这些文件分别放在对应的文件夹中
然后将文件的明细放在一个 .txt 文件中

"""
# 1 切换到需要遍历的文件夹
import os
import shutil
path = "fileCategory"
if not os.path.exists(path):
    print("路径有问题")
    exit()
# print(os.getcwd())
os.chdir(path)

# 2 遍历整个文件夹
file = os.listdir("./")
for fileName in file:
    # 3 获得每个文件的后缀名
    index = fileName.rfind(".")
    if index == -1:
        continue
    extension = fileName[index + 1:]
    # 4 查看以后缀名为名字的文件夹是否存在 如果存在就将文件移动到文件夹 如果不存在
    if extension not in file:
        os.mkdir(extension)
    # 则新建文件夹 并将文件移动到文件夹中
    shutil.move(fileName, extension)