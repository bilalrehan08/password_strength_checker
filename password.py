import re
import string

# List of common passwords
COMMON_PASSWORDS = ["123456", "password", "qwerty", "abc123", "letmein", "welcome", "123123", "admin", "password1", "1234"]

# List of keyboard patterns to avoid
KEYBOARD_PATTERNS = ["qwerty", "asdf", "zxcvbn", "qazwsx", "12345", "qwertyuiop", "qwerty123"]

def check_password_strength(password, username=None):
    # Check password length
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    # Check if it contains at least one uppercase letter
    if not re.search("[A-Z]", password):
        return "Weak: Password must have at least one uppercase letter."
    
    # Check if it contains at least one lowercase letter
    if not re.search("[a-z]", password):
        return "Weak: Password must have at least one lowercase letter."
    
    # Check if it contains at least one digit
    if not re.search("[0-9]", password):
        return "Weak: Password must have at least one digit."
    
    # Check if it contains at least one special character
    if not re.search("[@#$%^&+=]", password):
        return "Weak: Password must have at least one special character."
    
    # Check for repeated characters
    if len(password) != len(set(password)):
        return "Weak: Password must not contain repeated characters."
    
    # Check for consecutive numbers
    if any(password[i].isdigit() and password[i+1].isdigit() and int(password[i+1]) == int(password[i]) + 1 and password[i+2].isdigit() and int(password[i+2]) == int(password[i]) + 2 for i in range(len(password)-2)):
        return "Weak: Password must not contain three consecutive numbers."
    
    # Check against common passwords
    if password.lower() in COMMON_PASSWORDS:
        return "Weak: Password is too common and easily guessable."
    
    # Check for dictionary words (basic check, can be enhanced with a full dictionary)
    dictionary_words = ["password", "letmein", "admin", "welcome", "1234"]
    for word in dictionary_words:
        if word in password.lower():
            return f"Weak: Password contains common dictionary word: {word}."
    
    # Check if password contains personal information (like username)
    if username and username.lower() in password.lower():
        return "Weak: Password should not contain your username or personal information."
    
    # Check for keyboard patterns
    for pattern in KEYBOARD_PATTERNS:
        if pattern in password.lower():
            return f"Weak: Password contains a common keyboard pattern: {pattern}."
    
    # Check for repeated sequences
    if any(password[i:i+3] == password[i+3:i+6] for i in range(len(password)-5)):
        return "Weak: Password must not contain repeated sequences."
    
    # If it passes all checks, it's strong
    return "Strong: Password is good!"

if __name__ == "__main__":
    username = input("Enter your username (if applicable): ")
    password = input("Enter a password to check: ")
    result = check_password_strength(password, username)
    print(result)
