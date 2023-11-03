#hash method---------------

def three_sum_hash_method(nums):
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
                if two_sum in {nums[i], nums[j]} and two_sum in dictionary and \
                    dictionary[two_sum] > [nums[i], nums[j]].count(two_sum):
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


def three_sum_two_pointer_method(nums):
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        l = i+1
        r = len(nums)-1
        while l<r:
            print(i,nums[i]+nums[l]+nums[r], '--------iiiiiii--------')
            if nums[i]+nums[l]+nums[r] == 0:
                res.append([nums[i],nums[l],nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l-1] and l<r:
                    l += 1
                while nums[r] == nums[r+1] and l<r:
                    r -= 1
            elif nums[i]+nums[l]+nums[r] < 0:
                l += 1
                while nums[l] == nums[l-1] and l<r:
                    l += 1
            elif nums[i]+nums[l]+nums[r] > 0:
                r -= 1
                while nums[r] == nums[r+1] and l<r:
                    r -= 1
    return res

nums = [0,0,0]
# print(three_sum_hash_method(nums))
print(three_sum_two_pointer_method(nums))