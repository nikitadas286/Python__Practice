lst = [1, 2, 3, 2, 4, 1, 5, 3]
d={}
for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
    if d[i] > 1:
        print(i)