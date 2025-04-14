import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])

    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong ✅"
    elif score == 3:
        strength = "Moderate ⚠️"
    elif score == 2:
        strength = "Weak ❗"
    else:
        strength = "Very Weak ❌"

    print(f"\nPassword Strength: {strength}")
    print("Details:")
    if length_error: print("- Too short (min 8 characters)")
    if digit_error: print("- No digits")
    if uppercase_error: print("- No uppercase letters")
    if lowercase_error: print("- No lowercase letters")
    if symbol_error: print("- No special characters")

# Example usage:
password = input("Enter your password to check strength: ")
check_password_strength(password)
