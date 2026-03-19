# Password Strength Checker
# Coded by: Mr Sabaz Ali Khan Style 😄
# Date: March 2025

import re

def check_password_strength(password):
    """
    Checks password strength and returns score + feedback
    """
    # Initialize score
    score = 0
    feedback = []
    
    # ===== Basic Length Check =====
    if len(password) < 8:
        feedback.append("❌ Password should be at least 8 characters long")
    elif len(password) >= 12:
        score += 2
        feedback.append("✅ Good length")
    else:
        score += 1
        feedback.append("✔️ Okay length (better if ≥ 12)")
    
    # ===== Contains different character types =====
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};\'":\\|,.<>/?`~]', password))
    
    # Uppercase
    if has_upper:
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter (A-Z)")
    
    # Lowercase
    if has_lower:
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z)")
    
    # Numbers
    if has_digit:
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9)")
    
    # Special characters
    if has_special:
        score += 2   # special characters give more points
    else:
        feedback.append("❌ Add at least one special character (!@#$%^&*)")
    
    # ===== Bonus points =====
    # All four character types → bonus
    if has_upper and has_lower and has_digit and has_special:
        score += 2
        feedback.append("🎉 Excellent! All character types used")
    
    # Very long password bonus
    if len(password) >= 16:
        score += 1
        feedback.append("🏆 Very long password — good!")
    
    # ===== Common weak patterns =====
    weak_patterns = [
        r'123456', r'password', r'qwerty', r'abc123', r'111111',
        r'admin123', r'letmein', r'welcome123'
    ]
    
    for pattern in weak_patterns:
        if pattern in password.lower():
            score -= 3
            feedback.append(f"⚠️ Very common / weak pattern detected ({pattern})")
            break
    
    # ===== Final judgment =====
    if score >= 8:
        strength = "STRONG 💪"
        color = "green"
    elif score >= 5:
        strength = "MEDIUM ⚡"
        color = "orange"
    else:
        strength = "WEAK 😟"
        color = "red"
    
    # Print result
    print("\n" + "="*50)
    print(f"Password Strength: {strength}")
    print(f"Score: {score}/10")
    print("-"*50)
    
    for msg in feedback:
        print(msg)
    
    print("="*50 + "\n")
    
    return score, strength


# =======================
#       MAIN PROGRAM
# =======================
def main():
    print("🔐 PASSWORD STRENGTH CHECKER 🔐")
    print("Coded with ❤️ by Mr Sabaz Ali Khan style\n")
    
    while True:
        password = input("Enter your password (or 'q' to quit): ")
        
        if password.lower() == 'q':
            print("Thank you for using Password Strength Checker!")
            break
            
        if not password.strip():
            print("Error: Password cannot be empty!\n")
            continue
            
        check_password_strength(password)


if __name__ == "__main__":
    main()
