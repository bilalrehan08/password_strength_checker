import re
import string

COMMON_PASSWORDS = ["123456", "password", "qwerty", "abc123", "letmein", "welcome", "123123", "admin", "password1", "1234"]
KEYBOARD_PATTERNS = ["qwerty", "asdf", "zxcvbn", "qazwsx", "12345", "qwertyuiop", "qwerty123"]

def check_password_strength(password, username=None):
    analysis = []
    score = 0

    if len(password) >= 8:
        analysis.append("✓ Password length is sufficient.")
        score += 1
    else:
        analysis.append("✗ Password must be at least 8 characters long.")

    if re.search("[A-Z]", password):
        analysis.append("✓ Contains uppercase letter.")
        score += 1
    else:
        analysis.append("✗ Missing uppercase letter.")

    if re.search("[a-z]", password):
        analysis.append("✓ Contains lowercase letter.")
        score += 1
    else:
        analysis.append("✗ Missing lowercase letter.")

    if re.search("[0-9]", password):
        analysis.append("✓ Contains digit.")
        score += 1
    else:
        analysis.append("✗ Missing digit.")

    if re.search("[@#$%^&+=]", password):
        analysis.append("✓ Contains special character.")
        score += 1
    else:
        analysis.append("✗ Missing special character.")

    if len(password) == len(set(password)):
        analysis.append("✓ No repeated characters.")
        score += 1
    else:
        analysis.append("✗ Contains repeated characters.")

    if not any(password[i].isdigit() and password[i+1].isdigit() and int(password[i+1]) == int(password[i]) + 1 and password[i+2].isdigit() and int(password[i+2]) == int(password[i]) + 2 for i in range(len(password)-2)):
        analysis.append("✓ No consecutive numbers.")
        score += 1
    else:
        analysis.append("✗ Contains 3 consecutive numbers.")

    if password.lower() not in COMMON_PASSWORDS:
        analysis.append("✓ Not a common password.")
        score += 1
    else:
        analysis.append("✗ Password is too common.")

    dictionary_words = ["password", "letmein", "admin", "welcome", "1234"]
    if not any(word in password.lower() for word in dictionary_words):
        analysis.append("✓ No common dictionary words.")
        score += 1
    else:
        analysis.append("✗ Contains common dictionary words.")

    if not (username and username.lower() in password.lower()):
        analysis.append("✓ Does not contain personal information.")
        score += 1
    else:
        analysis.append("✗ Contains personal information (e.g. username).")

    if not any(pattern in password.lower() for pattern in KEYBOARD_PATTERNS):
        analysis.append("✓ No common keyboard patterns.")
        score += 1
    else:
        analysis.append("✗ Contains common keyboard patterns.")

    if not any(password[i:i+3] == password[i+3:i+6] for i in range(len(password)-5)):
        analysis.append("✓ No repeated sequences.")
        score += 1
    else:
        analysis.append("✗ Contains repeated sequences.")

    # Final assessment
    if score >= 10:
        verdict = "Strong: Password is very good!"
    elif score >= 7:
        verdict = "Moderate: Consider improving your password."
    else:
        verdict = "Weak: Your password is insecure."

    return verdict, analysis

if __name__ == "__main__":
    username = input("Enter your username (if applicable): ")
    password = input("Enter a password to check: ")
    verdict, feedback = check_password_strength(password, username)
    print("\nPassword Analysis Report:")
    for line in feedback:
        print(line)
    print("\nFinal Verdict:")
    print(verdict)
