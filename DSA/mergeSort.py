def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        x = merge_sort(left_arr)
        print(111111111)   
        y = merge_sort(right_arr)
        print(22222222222) 
        c = 1+2
        print(333333333)

arr = [3,5,2,1,8,9]
merge_sort(arr)