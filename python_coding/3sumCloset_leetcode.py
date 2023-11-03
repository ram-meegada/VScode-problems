# 16. 3Sum Closest

def three_sum_closest(nums, target):
    nums.sort()
    nearest = abs((nums[0]+nums[1]+nums[2]) - target)
    nearest_sum = nums[0]+nums[1]+nums[2]
    for i in range(len(nums)-2):
        l,r = i+1, len(nums)-1
        while l<r:
            summ = nums[i]+nums[l]+nums[r]
            if summ == target:
                return summ 
            elif summ < target:
                if abs(summ-target) < nearest:
                    nearest = abs(summ-target)
                    nearest_sum = summ
                l += 1
            elif summ > target:
                if abs(summ-target) < nearest:
                    nearest = abs(summ-target)
                    nearest_sum = summ
                r -= 1
    return nearest_sum      
nums = [0,1,2]
target = 1
result = three_sum_closest(nums, target)
print(result)