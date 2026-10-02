import random
import string

def generate_password(length=12):
    """Generate a strong random password"""
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    all_chars = letters + numbers + symbols
  # Create password
    password = "".join(random.choice(all_chars) for _ in range(length))
    return password
# Main Program
print("STRONG PASSWORD GENERATOR")

try:
    length = int(input("Enter password length (e.g., 12): "))
    
    if length < 4:
        print("Length should be at least 4")
    else:
        my_password = generate_password(length)
        print(f"\nYour Strong Password is: {my_password}")

except ValueError:
    print("Invalid input! Please enter a number like 12, 16, etc.")
    
