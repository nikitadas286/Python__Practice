a=[1,2,3,4,6]
b=[2,3,5,6,7]
a.extend(b)
c=[]
for i in a:
    if a.count(i)<2 and i not in c:
        c.append(i)
print("Uncommon elements:",c)