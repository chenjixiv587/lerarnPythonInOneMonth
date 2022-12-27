setOne = frozenset([1, 2, 3])
setTwo = {1, 3, 4}

# result = setTwo.intersection(setOne)

# result = setOne & setTwo


result = setTwo.intersection_update(setOne)
print(setTwo)
print(result)