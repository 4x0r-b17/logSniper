# system.py | for each given folder (path) finds system informations (country | language | timezone | os | hostname)
import os
from colorama import Fore, Style

def find_sys_info(base_path):
    sys_file_found = False
    for file in os.listdir(base_path):
        if os.path.isfile(os.path.join(base_path, file)) and "ystem.txt" in file: 
            sys_file_found = True
            full_path = os.path.join(base_path, file)
            system_version = user = time_zone = language = country = "N/A"
            with open(full_path, 'r') as f:
                try:
                    for line in f:
                        # timezone
                        if "zone" in line.lower() and ":" in line.lower():
                            parts = line.split(":", 1)
                            time_zone = parts[1].strip()
                        # os version
                        if "version" in line.lower() and ":" in line.lower():
                            parts = line.split(":", 1)
                            system_version = parts[1].strip()
                        # user
                        if "user" in line.lower() and ":" in line.lower():
                            parts = line.split(":", 1)
                            user = parts[1].strip()
                        elif "computer" in line.lower() and ":" in line.lower():
                            parts = line.split(":", 1)
                            user = parts[1].strip()
                        elif "hostname" in line.lower() and ":" in line.lower():
                            parts = line.split(":", 1)
                            user = parts[1].strip()
                        # country
                        if "country" in line.lower() and ":" in line.lower():
                            parts = line.split(":", 1)
                            country = parts[1].strip()
                        # language
                        if "language" in line.lower() and ":" in line.lower():
                            parts = line.split(":", 1)
                            language = parts[1].strip()
                except UnicodeDecodeError as e:
                    print(e)
            # country | language | timezone | os | user
            output = f"{Fore.GREEN}system info{Style.RESET_ALL}: {country} {Fore.RED}|{Style.RESET_ALL} {language} {Fore.RED}|{Style.RESET_ALL} {time_zone} {Fore.RED}|{Style.RESET_ALL} {system_version} {Fore.RED}|{Style.RESET_ALL} {user}"
    if not sys_file_found:
        output = f"{Fore.GREEN}system info{Style.RESET_ALL}: {Fore.YELLOW}404 not found{Style.RESET_ALL}"
    
    return output