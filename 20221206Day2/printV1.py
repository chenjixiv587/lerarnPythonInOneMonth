import time
print(1, 2, 3, sep="-", end="", flush=True)
# 将flush设置为True 就打破了 sleep 的限制 会立即输出
# 还有一张办法是 输出的内容里面加上 "\n" 或者保持end的默认值
# print() 输出的原理  先将内容输出到 缓存区 再输出到 控制台等
time.sleep(5)