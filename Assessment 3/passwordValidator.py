import re

def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    
    if not re.search("[a-z]", password):
        return False
    
    if not re.search("[0-9]", password):
        return False
    
    if not re.search("[A-Z]", password):
        return False
    
    if not re.search("[$#@]", password):
        return False
    
    return True

def validate_passwords(passwords):
    valid_passwords = []
    password_list = passwords.split(",")
    
    for password in password_list:
        if check_password(password):
            valid_passwords.append(password)
    
    return ",".join(valid_passwords)

# Example usage
#passwords_input = "Password1,pass123,HELLO123,$$pass$$,MyPass@12"
#valid_passwords_output = validate_passwords(passwords_input)
#print(valid_passwords_output)
