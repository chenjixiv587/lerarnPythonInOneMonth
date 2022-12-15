def sumNum(**args):
    # 字典
    print(args)
    for i in args:
        print(args[i])


sumNum(name="chen", age=12)