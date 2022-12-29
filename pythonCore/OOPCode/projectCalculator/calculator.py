# 实现一个计算器
# 实现语音播报
from win32com.client import Dispatch


# speaker = Dispatch("SAPI.SpVoice")
# speaker.Speak("你好")


class Calculator:

    def __speak(self, word):
        speaker = Dispatch("SAPI.SpVoice")
        speaker.Speak("{0}".format(word))

    def __makeDecorationSpeaker(word=""):
        def decorationSpeaker(func):
            def inner(self, num):
                self.__speak(word + str(num))
                return func(self, num)

            return inner

        return decorationSpeaker

    def __decorationCheck(func):
        def inner(self, num):
            if not isinstance(num, int):
                raise ValueError("不是一个整数")
            return func(self, num)

        return inner

    # 谁写在前面 就先装饰
    @__decorationCheck
    @__makeDecorationSpeaker()
    def __init__(self, firstNumber):
        self.__result = firstNumber

    @__decorationCheck
    @__makeDecorationSpeaker("加")
    def jia(self, v):
        self.__result += v
        return self

    @__decorationCheck
    @__makeDecorationSpeaker("减")
    def jian(self, v):
        self.__result -= v
        return self

    @__decorationCheck
    @__makeDecorationSpeaker("乘")
    def cheng(self, v):
        self.__result *= v
        return self

    @__decorationCheck
    @__makeDecorationSpeaker("除")
    def chu(self, v):
        self.__result /= v
        return self

    def show(self):
        # print("计算的结果是 {0}".format(self.__result))
        self.__speak("计算的结果是 {0}".format(self.__result))
        return self

    def clear(self):
        self.__result = 0
        return self

    @property
    def result(self):
        return self.__result


c1 = Calculator(1)
c1.jian(100).jia(90).cheng(77).show()

c2 = Calculator(441)
c2.jian(9)
c2.jia(10)
c2.show()

print(c2.result)
