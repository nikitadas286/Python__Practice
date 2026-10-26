str=input("Enter String:")

for ch in str:
    if str.count(ch)==1:
        print(ch)
        break