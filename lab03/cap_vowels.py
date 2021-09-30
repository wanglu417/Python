str1 = input("Please enter your own string: ").lower()
str2 = ""
vowels = ['a', 'e', 'i', 'o', 'u']
for i in str1:
    if i in vowels:
        str2 = str2+i.upper()
    else:
        str2 = str2+i

print(str2)
