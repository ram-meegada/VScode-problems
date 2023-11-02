def ans(nums):
    dictionary = {}
    for i in nums:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    res = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j == i:
                continue
            else:
                two_sum = -1*(nums[i] + nums[j])
                if two_sum in {nums[i], nums[j]} and two_sum in dictionary and dictionary[two_sum] > [nums[i], nums[j]].count(two_sum):
                    add = [nums[i],nums[j],two_sum]
                    add.sort()
                    if add not in res:
                        res.append(add)
                elif two_sum not in {nums[i], nums[j]} and two_sum in dictionary:
                    add = [nums[i],nums[j],two_sum]
                    add.sort()
                    if add not in res:
                        res.append(add)
    return res                        

nums = [-1,0,1,0]
print(ans(nums))