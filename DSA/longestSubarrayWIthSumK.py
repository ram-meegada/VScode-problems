def longestSubarrayWithSumK(a: [int], k: int) -> int:
    sum = 0
    for i in range(len(a)):
        do = []
        temp_sum = 0
        for j in range(i, len(a)):
            if temp_sum < k:
                temp_sum += a[j]
                do.append(a[j]) 
            elif temp_sum == k and a[j] == 0:
                do.append(0)
                if j == len(a)-1:
                    if len(do) > sum:
                        sum = len(do)
            elif temp_sum == k:
                if len(do) > sum:
                    sum = len(do)
                break
    return sum

k = 3
a = [1, 2, 3, 1, 1, 1, 1]
print(longestSubarrayWithSumK(a,k))