
from pathlib import Path

path = Path("C:/Users/jonat/Desktop/pcc_3e-main/chapter_10/reading_from_a_file/pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

a = 0
birth = input(f"Enter your birthday in the format (ddmm): ")

while True:
    test = pi_string[:(1 + a)]
    
    print(test)
    length = (len(test))
    
    if birth in str(test):
        print(f'Your birthday is in pi at the {length - 4} - {length - 1}th place')
        break
    a += 1
    