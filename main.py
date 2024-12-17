# Lucas Brinks
# 12/16/24
# Password Validation Code

password = input('Please enter your password: ')

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
        if char not in 'abcdefghijklmnopqrstuvwxyz1234567890':
            return
        return 'There cannot contain special characters or symbols.'
    
def check_for_number(password):
    for char in password:
        if char.isdigit():
            return
        return 'The password must contain at least one number'