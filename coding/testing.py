lst = [1,2,3,4,5,6]
for i in range((len(lst))//2):
    temp = lst[i]
    lst[i] = lst[len(lst)-i-1]
    lst[len(lst)-i-1] = temp
print(lst)    