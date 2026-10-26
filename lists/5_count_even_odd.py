a=[10,20,30,40,50,55,77,13,99 ]
even=0
odd=0
for i in a:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print("Even numbers:",even)
print("Odd numbers:",odd)