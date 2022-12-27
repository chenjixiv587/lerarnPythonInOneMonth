# 将“12-12-2022 12：23：12” 变为 "2022-12-12 12:23:12"

# 1 将格式化字符串日期 转换为 时间元组
# 2 将时间元组 转换为 格式化字符串

import time
TIME = "12-12-2022 12:23:12"
timeTuple = time.strptime(TIME, "%m-%d-%Y %H:%M:%S")
timeString = time.strftime("%Y-%m-%d %H:%M:%S", timeTuple)
print(timeString)
