a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

gcd=1
for i in range(1,a+1):
    if(a%i==0 and b%i==0):
        gcd=i
lcm=a*b//gcd
print("LCM of",a,"and",b,"is:",lcm)