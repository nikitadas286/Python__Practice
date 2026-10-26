a=[10,20,30,40,50,20,10,40,60,80,70,70,70,80]
b=[]
for i in a:
    if (a.count(i)>1) and i not in b:
        b.append(i)
print(b)