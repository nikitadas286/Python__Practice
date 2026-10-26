s="python is easy and python is powerful"
l=s.split(" ")
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)