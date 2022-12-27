# 实现在 发说说 和 发图片的时候  自动进行登录验证
def checkLogin(func):
    def inner():
        print("登录验证")
        func()

    return inner


@checkLogin
# 　这里的　＠checkLogin 相当于
# postSentence = checkLogin(postSentence)
def postSentence():
    print("发说说")


@checkLogin
# 当写上 @ 之后  装饰器就立即执行了 也即是说 目前postImage就是 inner
def postImage():
    print("发图片")


userButton = 1
if userButton == 1:
    postImage()
else:
    postSentence()
