ninePlusNine = ["{0} * {1} = {2}".format(j, i, i * j) for i in range(1,10) for j in range(1, i+1)]
print(ninePlusNine)

strPlusStr = [i+j for i in "qwe" for j in "asd"]
print(strPlusStr)