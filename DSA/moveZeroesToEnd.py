# 283. Move Zeroes
# Easy
# 15.4K
# 384
# Companies
# Given an integer array nums, move all 0's to the end of it while maintaining the 
# relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]

nums = [0]
i = 0
total = 0
while i<len(nums):
    if total == len(nums):
        print(nums, '-------- nums ------------')
        break
    if nums[i] == 0:
        x = nums.pop(i)
        nums.append(x)
        total += 1
    else:
        i += 1
        total += 1