import random
import string
import argparse

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    character_set = ''
    if use_uppercase:
        character_set += uppercase_letters
    if use_lowercase:
        character_set += lowercase_letters
    if use_digits:
        character_set += digits
    if use_symbols:
        character_set += symbols

    password = []

    for _ in range(length): 
        password.append(random.choice(character_set))

    random.shuffle(password)

    return ''.join(password)

def main():
    parser = argparse.ArgumentParser(description="Generate a password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument("-u", "--no-uppercase", action="store_false", help="Exclude uppercase letters")
    parser.add_argument("-w", "--no-lowercase", action="store_false", help="Exclude lowercase letters")
    parser.add_argument("-d", "--no-digits", action="store_false", help="Exclude digits")
    parser.add_argument("-s", "--no-symbols", action="store_false", help="Exclude symbols")
    args = parser.parse_args()

    password = generate_password(args.length, args.no_uppercase, args.no_lowercase, args.no_digits, args.no_symbols)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
