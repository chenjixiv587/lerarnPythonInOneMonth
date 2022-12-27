# 斐布拉切数
# 1 2 3 5 8 13

def fabric(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return fabric(n - 1) + fabric(n - 2)


print(fabric(6))
