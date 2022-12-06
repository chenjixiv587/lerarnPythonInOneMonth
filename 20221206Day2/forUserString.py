# 将用户输入的字符串 遍历打印出来

userString = input("Please type a sentence: ")
for character in userString:
    if character == "w":
        print(userString.index(character))