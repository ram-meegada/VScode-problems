# leetcode - 119
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]

class Solution:
    def pascal_triangle(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        else:
            nums = self.pascal_triangle(rowIndex-1)
            temp = [nums[i]+nums[i+1] for i in range(len(nums)-1)]
            temp.insert(0,1)
            temp.append(1)
            return temp

rowIndex = 3
result = Solution().pascal_triangle(rowIndex)
print(result)