import string

char = {}

print("Enter your sentence")
userin = input(">").lower()

for i in string.ascii_lowercase:
    print(i)
    char[i] = 0

print(char)

for i in userin:
    if i in char:
        char[i] += 1
isPangram = True

for letters in char:
    if char[letters] == 0:
        isPangram = False

if isPangram:
    print("String is a Pangram")
else:
    print("String is not a Pangram")