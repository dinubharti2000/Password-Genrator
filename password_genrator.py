import random

print("welcome! to the password genrator")

chars="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmi123456789!@#$%^&"

number=input("How many passwords want to genrate?: ")
number=int(number)

length=input("What is the lenght of passwords?: ")
length=int(length)

print("\nhere is your passwords:")

for pwd in range(number):
    passwords=''
    for c in range(length):
        passwords+=random.choice(chars)
    print(passwords)
