# Random Secure Password Generator
# Coded by: Mr. Sabaz Ali Khan ✦ 2025–2026 style
# Purpose: Generate strong, cryptographically secure random passwords

import secrets
import string
import argparse
import sys
from typing import Optional

def generate_password(
    length: int = 16,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    min_of_each: bool = True
) -> str:
    """
    Generate a strong random password using cryptographically secure randomness
    
    Args:
        length: Total password length (recommended: 14–24)
        use_upper: Include uppercase letters (A–Z)
        use_lower: Include lowercase letters (a–z)
        use_digits: Include numbers (0–9)
        use_symbols: Include special characters (!@#$%^&* etc.)
        min_of_each: Guarantee at least one character from each selected category
    
    Returns:
        A secure random password string
    """
    if length < 8:
        raise ValueError("Password length should be at least 8 characters")
    if length > 128:
        raise ValueError("Password length > 128 is usually unnecessary")

    # Character pools (avoiding confusing/ambiguous characters)
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits    = '0123456789'
    # Common safe symbols (avoiding < > ' " ` \ | that sometimes break copy-paste)
    symbols   = '!#$%&()*+,-./:;<=>?@[]^_{}~'

    # Build allowed character set
    allowed = ''
    if use_lower:   allowed += lowercase
    if use_upper:   allowed += uppercase
    if use_digits:  allowed += digits
    if use_symbols: allowed += symbols

    if not allowed:
        raise ValueError("At least one character type must be selected")

    # Generate base password using cryptographically secure random choices
    password = ''.join(secrets.choice(allowed) for _ in range(length))

    # Optional: guarantee at least one of each selected type
    if min_of_each:
        categories = []
        if use_lower:   categories.append(lowercase)
        if use_upper:   categories.append(uppercase)
        if use_digits:  categories.append(digits)
        if use_symbols: categories.append(symbols)

        # For each category → insert one guaranteed character at random position
        pos_list = secrets.SystemRandom().sample(range(length), len(categories))
        
        password_list = list(password)
        for pos, chars in zip(pos_list, categories):
            password_list[pos] = secrets.choice(chars)
        
        password = ''.join(password_list)

    return password


def main():
    parser = argparse.ArgumentParser(
        description="Strong Random Password Generator by Mr. Sabaz Ali Khan",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument("-l", "--length", type=int, default=16,
                        help="password length")
    parser.add_argument("--no-upper", action="store_false", dest="upper",
                        help="exclude uppercase letters")
    parser.add_argument("--no-lower", action="store_false", dest="lower",
                        help="exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_false", dest="digits",
                        help="exclude numbers")
    parser.add_argument("--no-symbols", action="store_false", dest="symbols",
                        help="exclude special characters")
    parser.add_argument("--no-guarantee", action="store_false", dest="guarantee",
                        help="do NOT force at least one of each type")
    parser.add_argument("-c", "--count", type=int, default=1,
                        help="how many passwords to generate")

    args = parser.parse_args()

    try:
        for i in range(args.count):
            pwd = generate_password(
                length=args.length,
                use_upper=args.upper,
                use_lower=args.lower,
                use_digits=args.digits,
                use_symbols=args.symbols,
                min_of_each=args.guarantee
            )
            print(pwd)
            
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()


# ───────────────────────────────────────────────
#           Quick usage examples:
# ───────────────────────────────────────────────
#
# Default (16 char strong password):
#   python password_gen.py
#
# 20 characters, no symbols:
#   python password_gen.py -l 20 --no-symbols
#
# 5 passwords of 18 chars (very strong):
#   python password_gen.py -l 18 -c 5
#
# Only letters (12 chars):
#   python password_gen.py -l 12 --no-digits --no-symbols
#
# ───────────────────────────────────────────────