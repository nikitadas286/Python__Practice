a=[100,10,20,30,40,50]
# print(min(a))

smallest=a[0]
for i in a:
    if i<smallest:
        smallest=i
print(smallest)