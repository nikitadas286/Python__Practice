a=[10,20,30,40,50,20,10]
# a.sort()
# print(a[-1])

# print(max(a))

largest=a[0]
for i in a:
    if i>largest:
        largest=i
print("Largest element is:", largest)