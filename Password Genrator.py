import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():
    print("Random Password Generator")
    length = int(input("Enter password length: "))
    password = generate_password(length)
    if password:
        print("Generated Password : ", password)

if _name_ == "_main_":
    main
