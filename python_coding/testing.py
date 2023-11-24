# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.
# Example 1:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

available_time_slots = [
    {"1": ("9:00", "9:30"), "availability":True},
    {"2": ("9:30", "10:00"), "availability":True},
    {"3": ("10:00", "10:30"), "availability":True},
    {"4": ("10:30", "11:00"), "availability":True},
    {"5": ("11:00", "11:30"), "availability":True},
    {"6": ("11:30", "12:00"), "availability":True},
    {"7": ("12:00", "12:30"), "availability":True},
    {"8": ("12:30", "13:00"), "availability":True},
]