# 偏函数的实际使用
import functools
num = "10001000"
# 把传入的 num当成二进制数 在转换为 十进制
result = int(num, base=2)
print(result)

intTwo = functools.partial(int, base=2)
print(intTwo(num))