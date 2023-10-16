# Input: ‘n’ = 5 ‘m’ = 3
# ‘a’ = [1, 2, 3, 4, 6]
# ‘b’ = [2, 3, 5]
# Output: [1, 2, 3, 4, 5, 6]

a = [1, 2, 3, 4, 6]
b = [2, 3, 5]
c = []
i=j=0
while i<len(a) and j<len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    elif a[i] > b[j]:
        c.append(b[j])
        j += 1
        
print(c)