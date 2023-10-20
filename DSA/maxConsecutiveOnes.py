# 485. Max Consecutive Ones
# Easy
# 5.2K
# 445
# Companies
# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3

nums = [1,1,0,1,1,1]
left = 0
max_count = 0
while left < len(nums):
    if nums[left] == 1:
        count = 0
        while left < len(nums) and nums[left] == 1:
            count += 1
            left += 1
        if count > max_count:
            max_count = count
    else:
        left += 1
print(max_count)