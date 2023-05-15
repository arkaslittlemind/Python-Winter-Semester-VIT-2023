import re

def validate_password(password):
    if len(password) < 6 or len(password) > 12:
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[$#@]", password):
        return False

    return True

def check_passwords(passwords):
    valid_passwords = []
    password_list = passwords.split(',')

    for password in password_list:
        password = password.strip()

        if validate_password(password):
            valid_passwords.append(password)

    return valid_passwords

passwords_input = input("Enter comma-separated passwords: ")
valid_passwords = check_passwords(passwords_input)

if valid_passwords:
    print("Valid passwords:", ', '.join(valid_passwords))
else:
    print("No valid passwords found.")
