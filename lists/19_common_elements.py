a=[1,2,3,4,6]
b=[2,3,5,6,7]
c=[]
a.extend(b)
for i in a:
    if a.count(i)>1 and i not in c:
        c.append(i)
print("Common Elements:", c)