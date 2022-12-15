def calculate(flag):
    def sumTotal(a, b):
        return a + b

    def jian(a, b):
        return a - b

    if flag == "+":
        return sumTotal
    else:
        return jian


res = calculate("+")(1, 2)
print(res)
