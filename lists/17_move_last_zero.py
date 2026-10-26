a=[0,10,20,30,40,0,80,60,0,12]
b=[]
c=[]
for i in a:
    if(i>0):
       b.append(i)
    else:
        c.append(i)

b.extend(c)
print(b)