def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x<pivot]
    right = [x for x in arr if x>pivot]
    middle = [x for x in arr if x==pivot]
    print(quick_sort(left) + middle + quick_sort(right), '--++++++++++')
    return quick_sort(left) + middle + quick_sort(right)

arr = [1,-1,0,2,-2,3,0]
print(quick_sort(arr))