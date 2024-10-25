from cryptography.fernet import Fernet

with open('passwords.txt','w') as f:
    f.write(f"Name: joe, Password: doe\n")
    print(f"Done")

with open('passwords.txt','r') as f:
    for line in f.readlines():
        print(line)