from win32com.client import Dispatch


# speaker = Dispatch("SAPI.SpVoice")
# speaker.speak("")


class Calculator:
    # 审核输入的数字
    def __check(func):
        def inner(self, v):
            if not isinstance(v, int):
                raise ValueError("不是整数")
            return func(self, v)

        return inner

    # 除数不能为0
    def __checkZero(func):
        def inner(self, v):
            if v == 0:
                raise ZeroDivisionError("除数不能为0")
            return func(self, v)

        return inner

    # 语音输出
    def __onlySpeak(self, word):
        speaker = Dispatch("SAPI.SpVoice")
        speaker.speak("{0}".format(word))

    def __speakWithWord(word=""):
        def __speakResult(func):
            def inner(self, v):
                self.__onlySpeak(word + str(v))
                return func(self, v)

            return inner

        return __speakResult

    @__check
    @__speakWithWord()
    def __init__(self, startNum):
        self.__result = startNum

    @__check
    @__speakWithWord("加")
    def jia(self, v):
        self.__result += v
        return self

    @__check
    @__speakWithWord("减")
    def jian(self, v):
        self.__result -= v
        return self

    @__check
    @__speakWithWord("乘")
    def cheng(self, v):
        self.__result *= v
        return self

    @__check
    @__checkZero
    def chu(self, v):
        self.__result /= v
        return self

    def clear(self):
        self.__result = 0
        return self

    @property
    def result(self):
        return self.__result


c = Calculator(12).jia(2).jian(2).cheng(200).chu(100)
print(c.result)
