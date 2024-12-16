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
    
print(check_length(password))
print(check_first_five(password))
print(check_last_three(password))