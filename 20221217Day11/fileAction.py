# r 只读文件 文件不存在就报错 第一次读取时指针在文件的最开始地方
with open("test.txt", "r") as f:
    f.seek(2, 0)
    print(f.tell())
    content = f.read()
    print(content)
    print(f.tell())

# r+ 读写操作 文件不存在就报错
# 如果在写之前没有进行读 那么就会覆盖以前的文字 但是 是有几位就覆盖几位 不会将以前的都清零
# 如果是在读取之后 在进行写入 那么就会在以前的内容后面进行写入 因为读取的时候 指针已经跑到后面了
with open("no1.txt", "r+") as f1:
    content1 = f1.read()
    print(content1)
    f1.write("hello world")

# w 只写操作 文件不存在会新建文件
# 写的内容会完全覆盖以前的内容,即清空以前的内容，再加入写入的内容
with open("no2.txt", "w") as f2:
    f2.write("wo")

# w+ 读写 如果先读的话 读取不到数据 因为数据都被覆盖了
# 如果先写的话 也读不到数据 因为指针跑后面了
# 所以这个没啥意义
with open("no3.txt", "w+") as f3:
    content3 = f3.read()
    print(content3)
    f3.write("f3")

# a 只写 在文件的后面追加文字
with open("no4.txt", "a") as f4:
    f4.write("append")

# a+ 如果先读的话 读取不到数据 因为指针在最后
# # 如果先写的话 也读不到数据 因为指针跑后面了
# # 所以这个没啥意义
with open("no5.txt", "a+") as f5:
    print(f5.read())
    f5.write("append.......")
    print(f5.read())

# rb 只读二进制文件
with open("as.jpg", "rb") as f6:
    content6 = f6.read()


# rb 只写二进制文件
# with open("b.jpg", "wb") as f7:
#     f7.write(content6[0: len(content6) // 2])


with open("b.jpg", "ab") as f8:
    f8.write(content6[len(content6) // 2: len(content6)])


# x  只负责创建文件
# with open("x.c.txt", "x") as f9:
#     pass
