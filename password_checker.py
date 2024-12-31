# Imports the `re` module, which provides support for working with regular expressions,allowing pattern matching and searching functionality used in the functions below.
import re

# Load common passwords from a file
def load_common_passwords(filepath):
    try:
        with open(filepath, 'r') as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        print("Wordlist file not found!")
        return set()

# Function to check for sequence match
def has_sequence_match(password, common_passwords):
    for common_password in common_passwords:
        for i in range(len(common_password) - 3):  # Check for sequences of 4 characters
            if common_password[i:i+4] in password:
                return True, common_password[i:i+4]
    return False, None

# Function to check password strength
def check_password_strength(password, common_passwords):
    feedback = []

    # Check for dictionary passwords
    if password in common_passwords:
        return "Weak", ["Your password is too common. Avoid using easily guessable passwords."]

    # Check for sequences in common passwords
    sequence_match, sequence = has_sequence_match(password, common_passwords)
    if sequence_match:
        return "Weak", [f"Password sequence '{sequence}' found in common passwords. Avoid such patterns."]

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. Use at least 8 characters.")
    if len(password) < 12:
        feedback.append("For stronger security, use 12 or more characters.")

    # Check character diversity
    if not re.search(r'[A-Z]', password):
        feedback.append("Add at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        feedback.append("Add at least one lowercase letter.")
    if not re.search(r'\d', password):
        feedback.append("Add at least one number.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Add at least one special symbol (!@#$%^&* etc.).")

    # Determine strength based on criteria
    if len(password) >= 12 and len(feedback) == 0:
        return "Strong", ["Your password is strong!"]
    elif len(password) >= 8 and len(feedback) <= 2:
        return "Moderate", feedback
    else:
        return "Weak", feedback

# Main function
def main():
    # Replace this with the path to your downloaded `10k-most-common.txt` file
    file_path = r"/content/10k-most-common.txt"
    common_passwords = load_common_passwords(file_path)

    password = input("Enter a password: ")
    strength, feedback = check_password_strength(password, common_passwords)

    print(f"Password Strength: {strength}")
    print("Feedback:")
    for item in feedback:
        print(item)

# Run the program
if __name__ == "__main__":
    main()
