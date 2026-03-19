# Advanced Password Generator
# Coded by: Mr. Sabaz Ali Khan
# Purpose: Create strong, customizable, and secure passwords
# Date: March 2026

import random
import string

def generate_password(length=12, 
                     use_upper=True, 
                     use_lower=True, 
                     use_digits=True, 
                     use_special=True):
    """
    Generate a secure random password with chosen character types
    
    Parameters:
        length (int): Length of password (recommended 12–20)
        use_upper (bool): Include uppercase letters A–Z
        use_lower (bool): Include lowercase letters a–z
        use_digits (bool): Include numbers 0–9
        use_special (bool): Include special characters !@#$%^&* etc.
    
    Returns:
        str: Generated password
    """
    
    # Define character pools
    lower_letters   = string.ascii_lowercase
    upper_letters   = string.ascii_uppercase
    digits          = string.digits
    special_chars   = "!@#$%^&*()-_=+[{]}|;:'\",<.>/?`~"
    
    # Build the total pool of allowed characters
    all_chars = ""
    if use_lower:
        all_chars += lower_letters
    if use_upper:
        all_chars += upper_letters
    if use_digits:
        all_chars += digits
    if use_special:
        all_chars += special_chars
    
    # Make sure user selected at least one character type
    if not all_chars:
        return "Error: You must select at least one character type!"
    
    # Guarantee at least one character from each selected type
    password = []
    
    if use_lower:
        password.append(random.choice(lower_letters))
    if use_upper:
        password.append(random.choice(upper_letters))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special_chars))
    
    # Fill the rest of the password length with random characters
    remaining_length = length - len(password)
    password += random.choices(all_chars, k=remaining_length)
    
    # Shuffle so the guaranteed characters are not always at start
    random.shuffle(password)
    
    # Convert list → string
    final_password = "".join(password)
    
    return final_password


def main():
    print("=======================================")
    print("   STRONG PASSWORD GENERATOR 2025     ")
    print("   Coded by Mr. Sabaz Ali Khan        ")
    print("=======================================\n")
    
    try:
        length = int(input("Enter password length (12–20 recommended): "))
        if length < 8:
            print("⚠️ Warning: Length < 8 is not secure!")
        elif length > 100:
            print("That's a very long password 😅")
    except:
        print("Invalid length → using default 16")
        length = 16
    
    print("\nChoose character types (y/n):")
    upper  = input("Include UPPERCASE letters? (Y/n): ").lower() != 'n'
    lower  = input("Include lowercase letters? (Y/n): ").lower() != 'n'
    digits = input("Include numbers (0-9)?        (Y/n): ").lower() != 'n'
    special= input("Include symbols (!@#$ etc)?   (Y/n): ").lower() != 'n'
    
    print("\n" + "─"*50)
    
    # Generate 4 strong passwords
    print("Here are your secure passwords:\n")
    
    for i in range(1, 5):
        pwd = generate_password(
            length=length,
            use_upper=upper,
            use_lower=lower,
            use_digits=digits,
            use_special=special
        )
        print(f"  {i})  {pwd}")
    
    print("\n" + "─"*50)
    print("Tip: Use a password manager and never reuse passwords!")
    print("Stay safe online 💻🔒\n")


if __name__ == "__main__":
    main()
