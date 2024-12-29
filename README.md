# Password Strength Checker

## Overview
The Password Strength Checker is a Python-based utility designed to evaluate the strength of passwords and provide actionable feedback. It helps users create strong passwords by identifying weaknesses and suggesting improvements.

## Features
- **Password Strength Evaluation**: Checks passwords for length, diversity, and inclusion of common patterns.
- **Feedback System**: Offers suggestions to improve password security.
- **Customizable Wordlist**: Includes a dictionary of common passwords for comparison.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/Teja-sai-praneeth/password-strength-checker.git
   ```
2. Download the `10k-most-common.txt` file from this repository or from any trusted source.

3. Replace the `file_path` in the `password_checker.py` script with the path where you saved the `10k-most-common.txt` file.

4. Navigate to the project directory:
   ```bash
   cd password-strength-checker
   ```
5. Run the script:
   ```bash
   python password_checker.py
   ```

## Sample Output
```
Enter a password: password123
Password Strength: Weak
Feedback:
- Your password is too common. Avoid using easily guessable passwords.
```

## Requirements
- Python 3.6 or later

## File Structure
```
password-strength-checker/
|
├── password_checker.py       # Main script
├── 10k-most-common.txt       # Common passwords wordlist (example file)
├── LICENSE                   # License file
├── README.md                 # Project documentation
└── .gitignore                # Git ignore file
```


