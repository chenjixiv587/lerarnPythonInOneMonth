import datetime

t1 = datetime.datetime.now()
t2 = datetime.datetime.today()
print(t1)
print(t2)

print(t1.year)
print(t1.month)

# 计算n天后的日期

tNow = datetime.datetime.today()
result = tNow + datetime.timedelta(days=7)
print(tNow, result)


# 得到两个日期时间之间的时间差

firstTime = datetime.datetime(2022, 1, 1, 12, 0, 0)
secondTime = datetime.datetime(2023, 1, 1, 12, 0, 0)
delta = secondTime - firstTime
print(delta, type(delta))
print(delta.total_seconds())
print(delta.days)
print(delta.seconds)