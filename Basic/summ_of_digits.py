num=int(input("Enter a number:"))
sums=0
while(num!=0):
    sums+=num%10
    num//=10
print("Sum is:",sums)