def ans(nums):
    res = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j == i:
                continue
            else:
                for k in range(len(nums)):
                    if k in [i, j]:
                        continue
                    else:
                        if (nums[i] + nums[j] + nums[k]) == 0:
                            add = [nums[i],nums[j],nums[k]]
                            add.sort()
                            if add not in res:
                                res.append(add)
    return res                        

nums = [-1,0,1,2,-1,-4]
# print(ans(nums))

def testing(lst, lst1):
    if lst == lst1:
        return True
    return False

lst = {1,2,3}
lst1 = {2,1,3}
d = {}
d[lst] = "set"
print(d)
print(testing(lst, lst1))