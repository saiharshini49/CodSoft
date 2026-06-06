import random
import string

def generate_password(length):
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine all characters
    all_characters = lowercase + uppercase + digits + special_chars

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


try:
    length = int(input("Enter the desired password length: "))

    if length <= 0:
        print("Please enter a positive number.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)

except ValueError:
    print("Invalid input! Please enter a number.")