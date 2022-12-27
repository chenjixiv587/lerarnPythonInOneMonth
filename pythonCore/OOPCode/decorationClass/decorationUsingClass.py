class Check:
    def __init__(self, func):
        self.f = func

    def __call__(self, *args, **kwargs):
        print("登录验证")
        self.f()


@Check
def show():
    print("give")


show()
