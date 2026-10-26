a=[10,85,21,25,74,65,145,85,965]

for i in range(1,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        else:
            j+=1
print(a)
