a=input("Enter a string:")
n=a
b=""
for i in a:
    b=i+b
if n==b:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")