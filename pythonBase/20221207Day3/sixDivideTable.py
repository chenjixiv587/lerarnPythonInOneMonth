# 66除法表
# 1 / 1 =
# 2 / 1 =   2/ 2 =
# 3 / 1 =   3/ 2 =  3/ 3 =

for i in range(1, 7):
    for j in range(1, i + 1):
        result = i / j
        print('{0} / {1} = {2:.2f}'.format(i, j, result), end='\t')
    print("")