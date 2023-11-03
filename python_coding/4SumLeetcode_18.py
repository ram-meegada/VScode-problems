# 18. 4Sum

def four_sum_leetcode(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j == i:
                continue 
            for i in range(len(nums)):
                for i in range(len(nums)):
                    pass



nums = [1, 0, -1, 0, -2, 2]
target = 0
result = four_sum_leetcode(nums, target)
print(result)