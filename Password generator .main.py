import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Characters to choose from
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least one lowercase, one uppercase, one digit, and one special character
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the result to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Example usage
print("Generated Password:", generate_password(16))

