def generateLines(content, length):
    def makeLines():
        print("-" * (length // 2) + content + "-" * (length // 2))

    return makeLines


line1 = generateLines("hello", 10)
line1()

line2 = generateLines("world", 20)
line2()