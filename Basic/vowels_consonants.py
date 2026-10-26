a=input("Enter String:")
vowels=0
consonants=0

for ch in a.lower():
    if ch.isalpha():
        if ch in 'aeiou':
            vowels=vowels+1
        else:
            consonants=consonants+1
print("Vowels are:" ,vowels)
print("Consonanats are :" ,consonants)