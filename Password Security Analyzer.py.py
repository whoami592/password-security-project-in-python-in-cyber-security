# ========================================================
#   PASSWORD SECURITY ANALYZER
#   Coded by Mr. Sabaz Ali Khan
#   Version: 1.2 (March 2026)
#   Pure Python - No external dependencies required
# ========================================================

import re
import getpass
import math
import sys

# Common weak passwords (expanded list - 50+ most common ones)
COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "abc123", "password1",
    "admin", "letmein", "welcome", "monkey", "login", "princess",
    "rockyou", "abc123", "iloveyou", "111111", "123123", "sunshine",
    "12345678", "qwerty123", "admin123", "password123", "football",
    "baseball", "welcome123", "ninja", "abc123456", "master", "hello",
    "freedom", "whatever", "dragon", "mustang", "trustno1", "michael",
    "shadow", "superman", "batman", "starwars", "qwertyuiop", "1234567890",
    "654321", "iloveyou1", "password1", "1234", "12345", "000000",
    "696969", "jesus", "jesus1", "qazwsx", "qazwsxedc", "zaq1zaq1"
}

def calculate_entropy(password: str) -> float:
    """Calculate approximate password entropy in bits"""
    if not password:
        return 0.0
    
    # Detect character sets
    lower = bool(re.search(r'[a-z]', password))
    upper = bool(re.search(r'[A-Z]', password))
    digits = bool(re.search(r'[0-9]', password))
    special = bool(re.search(r'[^A-Za-z0-9]', password))
    
    charset_size = 0
    if lower: charset_size += 26
    if upper: charset_size += 26
    if digits: charset_size += 10
    if special: charset_size += 32  # common special chars
    
    if charset_size == 0:
        charset_size = 95  # fallback for full printable
    
    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)

def analyze_password(password: str) -> dict:
    """Main analysis function - returns detailed report"""
    if not password:
        return {"strength": "Invalid", "score": 0, "feedback": ["Empty password!"], "entropy": 0.0}
    
    score = 0
    feedback = []
    issues = []
    suggestions = []
    
    # 1. Length Check
    length = len(password)
    if length >= 16:
        score += 5
        feedback.append("✅ Excellent length (16+ characters)")
    elif length >= 12:
        score += 4
        feedback.append("✅ Good length (12+ characters)")
    elif length >= 8:
        score += 2
        feedback.append("⚠️  Acceptable length (8+ characters)")
    else:
        issues.append("Too short")
        suggestions.append("• Make it at least 12 characters long")
        feedback.append("❌ Password is too short")
    
    # 2. Character Variety
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[^A-Za-z0-9]', password))
    
    variety_score = 0
    if has_lower:
        variety_score += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        suggestions.append("• Add lowercase letters (a-z)")
    
    if has_upper:
        variety_score += 1
        feedback.append("✅ Contains uppercase letters")
    else:
        suggestions.append("• Add uppercase letters (A-Z)")
    
    if has_digit:
        variety_score += 1
        feedback.append("✅ Contains numbers")
    else:
        suggestions.append("• Add digits (0-9)")
    
    if has_special:
        variety_score += 2
        feedback.append("✅ Contains special characters")
    else:
        suggestions.append("• Add special characters (!@#$%^&*)")
    
    score += variety_score
    
    # 3. Common Password & Pattern Detection
    lower_pw = password.lower()
    if lower_pw in COMMON_PASSWORDS or any(common in lower_pw for common in COMMON_PASSWORDS):
        score -= 6
        feedback.append("❌ Extremely common password detected!")
        suggestions.append("• NEVER use common passwords like 'password123'")
    
    # Sequential patterns (123, abc, qwe, etc.)
    if re.search(r'123|abc|qwe|asd|zxc|qwerty|asdf', lower_pw):
        score -= 3
        feedback.append("❌ Sequential pattern detected")
        suggestions.append("• Avoid keyboard sequences")
    
    # Repeated characters
    if re.search(r'(.)\1{2,}', password):
        score -= 2
        feedback.append("❌ Repeated characters (aaa, 111)")
        suggestions.append("• Avoid repeating the same character")
    
    # Only numbers or only letters
    if password.isdigit():
        score -= 4
        feedback.append("❌ Only numbers - very weak")
    elif password.isalpha():
        score -= 3
        feedback.append("❌ Only letters - very weak")
    
    # 4. Entropy (bits)
    entropy = calculate_entropy(password)
    if entropy > 80:
        feedback.append(f"✅ Extremely high entropy ({entropy} bits)")
    elif entropy > 60:
        feedback.append(f"✅ Strong entropy ({entropy} bits)")
    elif entropy > 40:
        feedback.append(f"⚠️  Medium entropy ({entropy} bits)")
    else:
        feedback.append(f"❌ Low entropy ({entropy} bits)")
        suggestions.append("• Increase length and character variety")
    
    # Final Strength Rating
    if score >= 12:
        strength = "🔥 VERY STRONG"
        color = "GREEN"
    elif score >= 9:
        strength = "🟢 STRONG"
        color = "GREEN"
    elif score >= 6:
        strength = "🟡 MEDIUM"
        color = "YELLOW"
    elif score >= 3:
        strength = "🟠 WEAK"
        color = "ORANGE"
    else:
        strength = "🔴 VERY WEAK"
        color = "RED"
    
    # Final report dictionary
    return {
        "strength": strength,
        "score": max(0, min(15, score)),  # cap between 0-15
        "entropy": entropy,
        "feedback": feedback,
        "suggestions": suggestions,
        "color": color
    }

def print_colored(text: str, color: str):
    """Simple ANSI color support"""
    colors = {
        "GREEN": "\033[92m",
        "YELLOW": "\033[93m",
        "ORANGE": "\033[33m",
        "RED": "\033[91m",
        "RESET": "\033[0m"
    }
    print(f"{colors.get(color, '')}{text}{colors['RESET']}")

def main():
    print("=" * 60)
    print("🔐 PASSWORD SECURITY ANALYZER")
    print("   Coded by Mr. Sabaz Ali Khan")
    print("=" * 60)
    print("Type 'quit' or 'exit' to stop\n")
    
    while True:
        try:
            password = getpass.getpass("🔑 Enter password to analyze: ")
            
            if password.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Thank you for using Password Security Analyzer!")
                break
                
            if not password.strip():
                print("❌ Please enter a password!\n")
                continue
                
            # Analyze
            result = analyze_password(password)
            
            print("\n" + "=" * 60)
            print_colored(f"RESULT: {result['strength']}", result['color'])
            print(f"Score      : {result['score']}/15")
            print(f"Entropy    : {result['entropy']} bits")
            print("=" * 60)
            
            print("\n📋 ANALYSIS:")
            for line in result['feedback']:
                print("   " + line)
            
            if result['suggestions']:
                print("\n💡 RECOMMENDATIONS TO IMPROVE:")
                for sug in result['suggestions']:
                    print("   " + sug)
            
            # Real-world advice
            print("\n🌐 Pro Tip:")
            print("   Check if your password was leaked at: haveibeenpwned.com")
            print("=" * 60 + "\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"⚠️  Error: {e}")

if __name__ == "__main__":
    main()