lst = [1,2,3,2,1,1,1]
hash_lst = len(lst)*[0]

for i in lst:
    hash_lst[i] += 1
print(hash_lst)    