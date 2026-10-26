str1=input("Enter a string: ")
str2=input("Enter a string: ")

if  sorted(str1.lower())==sorted(str2.lower()):
    print("Anagram")
else:
    print("Not an Anagram")