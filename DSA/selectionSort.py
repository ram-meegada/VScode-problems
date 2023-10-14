lst = [-1,5,4,1,6]

for i in range(len(lst)):
    min = i
    for j in range(i,len(lst)):
        if lst[j] < lst[min]:
            min = j
    temp = lst[i]
    lst[i] = lst[min]         
    lst[min] = temp

print(lst)    