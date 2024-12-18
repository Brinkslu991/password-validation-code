# Lucas Brinks
# 12/16/24
# Password Validation Code



def check_length(password):
    if len(password) < 8:
        return 'Your password must be 8 characters long.'
    else:
        return

def check_first_five(password):
    if len(password) >= 5 and password[:5].isalpha():
        return
    else:
        return 'The first five characters must be letters only.'

def check_last_three(password):
    if len(password) >= 3 and password[-3:].isdigit():
        return 
    else:
        return'The last three characters must be numbers only.'
    
def check_for_letter(password):
    for char in password:
        if char.isalpha():
            return 
    return 'There must be at least one letter in your password.'
    
def check_no_special_characters(password):
    for char in password:
        if not char.isalnum():
            return 'There can not be any special characters.'
        
def check_for_number(password):
    for char in password:
        if char.isdigit():
            return None
    return 'The password must contain at least one number'
    
def main():
    password = input('Please enter your password: ')
    errors = []
    checks = [check_length(password),check_first_five(password),check_last_three(password),check_for_letter(password),check_no_special_characters(password),check_for_number(password)]
    for result in checks:
        if result is not None:
            errors.append(result)
        
    if errors:
        for error in errors:
            print(error)
    else:
        print(f'Your password is: {password}')

if __name__ == '__main__':
    main()
