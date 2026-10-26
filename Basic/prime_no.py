import math

a=int(input("Enter a number tocheck prime or not: "))
if a<=1:
    print(a,"Not a prime Number")
else:
    is_prime=True
    for i in range(2,int(math.sqrt(a))+1):
        if(a%i==0):
            is_prime=False
            break
    if is_prime:
        print(a,"prime Number")
    else:
        print(a,"Not a prime number")