num=int(input("Enter a number:"))
digits_len=len(str(num))
a=num
add=0
while(num!=0):
    digit=num%10
    add+=digit**digits_len
    num//=10
if(a==add):
    print("Armstrong Number")
else:
    print("Not an armstrong number")