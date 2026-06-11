import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter the desired password length: "))

# Character sets
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + numbers + symbols

# Generate password
password = ""

for i in range(length):
    password += random.choice(all_characters)

print("\nGenerated Password:")
print(password)
