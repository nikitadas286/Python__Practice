a=input("enter string:")
cnt=0

for ch in set(a):
    print(ch,":",a.count(ch))