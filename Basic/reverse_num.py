num=int(input("Enter a number:"))
rev=0
while(num!=0):
    rev=num%10+rev*10
    num=num//10
print("Reverse Number:",rev)