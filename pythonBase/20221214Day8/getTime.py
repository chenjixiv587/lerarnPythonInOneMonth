# 获取时间戳
import time
print(time.time())

print(time.localtime())


print(time.ctime(time.time()))
print(time.asctime(time.localtime()))

formatDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
tupleTime = time.strptime(formatDate, "%Y-%m-%d %H:%M:%S")
print(tupleTime)
print(time.mktime(tupleTime))