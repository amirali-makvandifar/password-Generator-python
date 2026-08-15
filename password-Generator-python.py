import random

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*"

characters = letters + numbers + symbols

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice(characters)

print("Your password is:", password)