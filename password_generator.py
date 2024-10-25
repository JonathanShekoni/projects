import random
import string

def generate_password(min_length,digits = True,characters = True):
    letters = string.ascii_letters
    numbers = string.digits
    special_characters = string.punctuation
    password = ""
    options = letters
    if digits:
        options += numbers
    if characters:
        options +=  special_characters
        
    
    pwd = password.join(random.choices(options, k = min_length))
    return pwd

length = int(input(f"How long do you want your password to be: "))
has_digits = input(f"Do you want your password to contain digits?(Y/N): ").lower() == 'y'
has_char = input(f"Do you want your password to contain characters?(Y/N): ").lower() == 'y'


password = generate_password(length,has_digits,has_char)
print(f"Your password is {password}")

