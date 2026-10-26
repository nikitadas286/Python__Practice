num=int(input("Enter a number: "))
a=0
b=1
if num<=0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(num):
        print(a)
        c=a+b
        a=b
        b=c