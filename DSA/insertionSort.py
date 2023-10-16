# like arranging deck of cards. we pick record from unsorted array
# and place in the correct position of sorted array

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = i-1
        ele = arr[i]
        while(key > -1 and arr[key]>ele):
            arr[key+1] = arr[key]
            key -= 1
        arr[key+1] = ele

my_array = [1, 4, 7, 1, 9, 0]
insertion_sort(my_array)
print(my_array)