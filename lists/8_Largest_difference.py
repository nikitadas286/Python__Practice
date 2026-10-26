a=[10,20,30,40,50,100]
# a.sort()
# print(a[-1]-a[0])

smallest=a[0]
largest=a[0]
for i in a:
    if i<smallest:
        smallest=i
    if i>largest:
        largest=i
print("largestDifference is :", largest-smallest)