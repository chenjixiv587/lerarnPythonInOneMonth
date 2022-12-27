# 将一个文件复制到另一个副本中
# 1 以只读模式打开一个文件  并且读取这个文件的内容
# 2 创一个副本 以 a 的模式
# 3 将第一个文件的内容写入到第二个中


with open("hello.txt", "r", encoding="utf-8") as srcFile:
    while True:
        contentSrcFile = srcFile.read(1024)
        with open("helloCopy.txt", "a", encoding="utf-8") as dstFile:
            dstFile.write(contentSrcFile)
        # print(contentSrcFile)
        if len(contentSrcFile) == 0:
            break



