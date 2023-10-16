def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)
        
        i,j,k =0,0,0
        while i<len(left_arr) and j<len(left_arr):
            if left_arr[i]<right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            elif left_arr[i]>right_arr[j]:
                arr[k] = right_arr[j]
                j += 1    
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1        
        print(arr, '------------')
    return arr

arr = [3,-1,2,1,8,0,-2,-3]
x = merge_sort(arr)
print(x)