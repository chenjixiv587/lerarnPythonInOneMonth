myList = [1, 3, 33, 4, 5, 6, 4, 6, 4]
# del myList[2]
# myList.remove(1)
# myList.pop()

# 删除列表中 所有的 4
# while True:
#     myList.remove(4)
#     if 4 not in myList:
#         break
#　wrong way
nums = [1, 2, 2, 2, 4, 2]
for num in nums:
    if num == 2:
        nums.remove(num)
print(nums)