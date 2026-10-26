str=input("Enter String:")
max_count=0
max_char=""

for ch in str:
    count=str.count(ch)
    if(count>max_count):
        max_count=count
        max_char=ch
print("Most frequent character is:", max_char, "with count:", max_count)