"""
A simple password management system using Fernet encryption for securely storing passwords.

Features: 
- add new passwords
- view stored passwords 
- encrypted password storage in a file.

"""

import os
from cryptography.fernet import Fernet

def write_key(): # Generates a new encryption key and saves it to a file, only if the key does not already exist.

    if not os.path.exists("./mykey.key"):
        key = Fernet.generate_key()
        with open("./mykey.key", "wb") as f:
            f.write(key)
        print("New key generated and saved to mykey.key.")
    else:
        print("Key already exists. No need to generate a new one.")


def load_key(): # Loads the encryption key from the file.
    
    with open("./mykey.key", "rb") as f:
        return f.read() 
    

# Generate key only if it does not exist
write_key()

# Load the encryption key
key = load_key()
fernet = Fernet(key)


def add_pass(username, password): # Adds a new username and encrypted password to the password file.

    with open("./password.txt", "a") as f:
        encrypted_pss = fernet.encrypt(password.encode()).decode()
        f.write(f"{username}|{encrypted_pss}\n")
    print("Added!")


def view_pass(): # Decrypts and prints all usernames and passwords from the password file.
    
    try:
        with open("./password.txt", "r") as f:
            for item in f:
                item = item.rstrip()
                if item:  # Ensure it's not an empty line
                    username, encrypted_password = item.split("|")
                    password = fernet.decrypt(encrypted_password.encode()).decode()
                    print(f"Username: {username} | Password: {password}")
    except FileNotFoundError:
        print("No passwords found. Add some passwords first.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main loop for user input
while True:
    user_input = input("Enter the mode (v: view, a: add, q: quit): ")

    if user_input == "v":
        print("Your passwords are as follows:")
        view_pass()

    elif user_input == "a":
        print("Let's add a new username and password")
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        add_pass(username, password)

    elif user_input == "q":
        break

    else:
        print("Invalid mode! Please enter 'v', 'a', or 'q'.")
