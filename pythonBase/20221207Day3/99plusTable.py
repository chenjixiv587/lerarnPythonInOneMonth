# 99 乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        result = j * i
        print('{0} X {1} = {2}'.format(j, i, result), end="\t")
    print()