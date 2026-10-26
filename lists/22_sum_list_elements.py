a=[1,2,3,4,5,6,7,8]
target=10

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]+a[j]==target):
            print("Pairs are:",a[i],a[j])
        else:
            j+=1
