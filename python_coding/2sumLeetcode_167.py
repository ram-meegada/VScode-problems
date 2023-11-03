# 167. Two Sum II - Input Array Is Sorted

def two_sum_leetcode(nums, target):
    l,r = 0,len(nums)-1
    while l<r:
        if nums[l] + nums[r] == target:
            return [l+1, r+1]
        elif nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:    
            l += 1
    return []        

nums = [-1, 0]
target = -1
result = two_sum_leetcode(nums, target)
print(result)