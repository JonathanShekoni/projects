import random
from pathlib import Path
import json
import string

# Define the path and options
path = Path('Personal/files/rlusername.json')
options_0 = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '$', '.', '%', '#', '!', '@', '.'
]

# Generate the password
length = int(input(f"How long do you want your password to be? "))
password = ''.join(random.choices(options_0, k=length))
finished = password.title()

# Collect user input
print(f"Your password is: {finished}")
user = input("Input your username for the password: ")
website = input("Which website is this for? ")

# Store the information
info = {'username': user, 'password': finished, 'website': website}

# Ensure the directory exists
path.parent.mkdir(parents=True, exist_ok=True)

# Load existing data if the file exists, otherwise start with an empty list
if path.exists():
    try:
        with path.open('r', encoding='utf-8') as file:
            data = json.load(file)
            
            # Check if data is a dictionary (this is incorrect, convert to a list)
            if isinstance(data, dict):
                data = [data]
                
    except json.JSONDecodeError:
        data = []  # Handle case where the file is empty or corrupt
else:
    data = []

# Append the new info to the data
data.append(info)

# Write the updated data back to the file
with path.open('w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)
