# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent
# , with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

def solution(nums):
    l = 0 
    r = len(nums)-1
    while l < r:
        if nums[l] > nums[r]:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            r -= 1
        elif nums[l] < nums[r]:
            l += 1
        else:
            l += 1
            r -= 1
    return nums

nums = [1,0,2]
result = solution(nums)
print(result)