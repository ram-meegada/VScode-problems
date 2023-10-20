# Input: ‘n’ = 5 ‘m’ = 3
# ‘a’ = [1, 2, 3, 4, 6]
# ‘b’ = [2, 3, 5]
# Output: [1, 2, 3, 4, 5, 6]

a = [1, 35]
b = [6, 9, 13, 15, 20, 25, 29, 46]
c = {}
i=j=0
while i<len(a) and j<len(b):
    if a[i] < b[j]:
        c[a[i]] = 1
        i += 1
    elif a[i] > b[j]:
        c[b[j]] = 1
        j += 1
    else:
        c[b[j]] = 1
        i += 1
        j += 1    

while i<len(a):
    c[a[i]] = 1
    i += 1
while j<len(b):    
    c[b[j]] = 1
    j += 1
print(list(c.keys()))