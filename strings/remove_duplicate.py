str=input("Enter String:")
new_str=""
for ch in str:
    if ch not in new_str:
        new_str+=ch
print("String after removing duplicates:", new_str)