# credentials.py | this script finds the credentials (USER:PASSWORD) linked to a target path and for a specific website
import os
from colorama import Fore, Style

def process_password_file(path, word, seen_credentials):
    try:
        with open(path, 'r') as p:
            lines = p.readlines()
        
        for i in range(len(lines) - 2):
            line = lines[i].strip()
            user = lines[i + 1].strip()
            password = lines[i + 2].strip()
            if word in line and "NOT_SAVED" not in password:
                key = (user, password)
                if key not in seen_credentials:
                    seen_credentials.add(key)
                    output = f"{Fore.RED}credentials:{Style.RESET_ALL} {user} {Fore.RED}|{Style.RESET_ALL} {password}"
                    return output
    except Exception as e:
        pass  # silently ignore if the file can't be opened

def find_credentials(target_path, word):
    seen_credentials = set()
    filenames = ["All Passwords.txt", "Passwords.txt", "passwords.txt"]

    for fname in filenames:
        path = os.path.join(target_path, fname)
        output = process_password_file(path, word, seen_credentials)
        return output

    if not seen_credentials:
        output = f"{Fore.RED}credentials:{Style.RESET_ALL} 404 not found"
    