import re

def check_password_strength(password):
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

    # If it passes all checks, it's strong
    return "Strong: Password is good!"

if __name__ == "__main__":
    password = input("Enter a password to check: ")
    result = check_password_strength(password)
    print(result)
