class Person:
    # 实例方法
    def eat(self):
        print(self)

    # 类方法
    @classmethod
    def functionClass(cls):
        print(cls)

    # 静态方法
    @staticmethod
    def functionStatic():
        print("static")


p = Person()
p.eat()
Person.functionStatic()
Person.functionClass()
