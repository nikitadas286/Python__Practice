# a=list(map(int,input("Enter Element:").split()))     #user input list
a=[1,2,3,4,5,6,7,8]
k=int(input("Enter number of rotations:"))
print(a[k:]+a[:k])
