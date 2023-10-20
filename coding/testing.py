nums = set([0,3,1])

for i in range(len(nums)+1):
    if i not in nums:
        print(i)
        break