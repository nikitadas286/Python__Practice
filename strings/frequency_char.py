str=input("Enter String:")

for ch in set(str):
    print(ch,":",str.count(ch))