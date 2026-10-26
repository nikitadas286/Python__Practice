a=[1,2,3,4,5,6,1,2,3]
k=int(input("Enter k value for largest element:"))
b=[]
for i in a:
    if i not in b:
        b.append(i)
b.sort()
print(b)
print(b[-k])