import re

# Load common passwords from a file
def load_common_passwords(filepath):
    try:
        with open(filepath, 'r') as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        print("Wordlist file not found!")
        return set()

# Function to check password strength
def check_password_strength(password, common_passwords):
    feedback = []

    # Check for dictionary passwords
    if password in common_passwords:
        return "Weak", ["Your password is too common. Avoid using easily guessable passwords."]

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
    # Use the full path to the file
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
