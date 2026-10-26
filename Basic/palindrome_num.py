num=int(input("Enter a number:"))
a=num
rev=0
while(num!=0):
    rev=num%10+rev*10
    num=num//10
if(a==rev):
    print("Palindrome number")
else:
    print("Not a palindrome number")