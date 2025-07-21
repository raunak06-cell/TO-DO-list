import random
import string

def generate_password():
    print("🔐 Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("❗ Please enter a positive number.")
            return
    except ValueError:
        print("❗ Invalid input. Please enter a number.")
        return

    # Define character sets
    letters = string.ascii_letters   # a-zA-Z
    digits = string.digits           # 0-9
    symbols = string.punctuation     # Special characters

    # Combine all characters
    all_chars = letters + digits + symbols

    # Randomly generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    print(f"\n✅ Generated Password: {password}")

# Run the password generator
generate_password()
