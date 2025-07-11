# cookies.py | this file search for cookies associated with credentials
import os
import subprocess
from colorama import Fore, Style
from collections import defaultdict

def find_cookie(target_path, word, target_folder):
    cookie_found = False
    command = f"grep -r '{word}' '{target_path}' | grep -n --color=auto 'ookie'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    # matches counter
    match_counts = defaultdict(int)

    # Main folder for all cookies
    main_cookie_folder = os.path.join(os.getcwd(), "main_cookies")
    os.makedirs(main_cookie_folder, exist_ok=True)

    # Site-specific folder (for each website/word)
    site_folder = os.path.join(main_cookie_folder, f"{word}")
    os.makedirs(site_folder, exist_ok=True)

    # Initialize log path but will only write if cookies are found
    log_path = os.path.join(site_folder, f"{target_folder}.txt")

    # Check for cookies and write to file only if found
    for line in result.stdout.splitlines():
        parts = line.split(':', 2)  # splitting at most 2 parts -> [part1, part2, part3]
        if len(parts) >= 2:
            cookie = parts[-1]
            full_path = parts[1].strip()

            if "ookie" in full_path.lower():
                cookie_found = True
                full_dir = os.path.dirname(full_path)  # Get only the file's directory  
                parts = full_dir.split("/")
                
                while parts and 'target' not in parts[-1]:
                    parts.pop()
                    
                if parts:
                    target_path = os.path.join(*parts)
                    match_counts[target_path] += 1
                    # Write cookie data to file if cookies are found
                    with open(log_path, "a") as log_file:
                        log_file.write(cookie + '\n')

    # Print results if cookies are found
    if cookie_found:
        for folder, count in match_counts.items():
            output = f"{Fore.GREEN}cookies{Style.RESET_ALL}: {Fore.YELLOW}{count}{Style.RESET_ALL} matches"
    else:
        output = f"{Fore.GREEN}cookies{Style.RESET_ALL}: {Fore.GREEN}404 not found{Style.RESET_ALL}"       
        
    return output