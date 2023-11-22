# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

n = 5
for i in range(1, n+1):
    if i % 2 == 0:
        lst = i * [0,1]
    else:
        lst = i * [1,0]
    for j in range(i):
        print(lst[j], end=' ')
    print()