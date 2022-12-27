myList = [("q", 2), ("w", 4), ("o", 9)]


def getKey(t):
    return t[1]


sortedList = sorted(myList, key=getKey, reverse=True)
print(sortedList)
myList.sort(key=getKey, reverse=True)
print(myList)