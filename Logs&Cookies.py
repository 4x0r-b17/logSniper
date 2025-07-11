# Logs&Cookies.py | script that find credential for specific websites with matching cookie

import os
import pyfiglet
import argparse
import subprocess
import shutil
from system import find_sys_info
from colorama import Fore, Style
from cookies import find_cookie
from credentials import find_credentials
from collections import defaultdict

# ------- main process automation
def automate(words, path):
    seen_folders = set()
    match_counts = defaultdict(int)
    used = []
    for w in words:
        word = w.strip()
        used.append(word)
        print(f'[!] Word looking for: {word}')
        command = f"grep -r '{word}' {path} | grep -n --color=auto 'sswords.txt'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        for line in result.stdout.splitlines():
            parts = line.split(':', 2)      # will be done at most 2 splits -> [part1, part2, part3]
            if len(parts) >= 2:
                full_path = parts[1] if parts[0].isdigit() else parts[0]
                full_path = full_path.strip()
                if "all password" in full_path.lower():
                    full_dir = os.path.dirname(full_path)   # get only the file's directory  
                    parts = full_dir.split("/")
                    while parts and 'target' not in parts[-1]:
                        parts.pop()
                    if not parts:
                        continue
                    target_path = os.path.join(*parts)
                    target_folder = parts[-1]
                    if target_path not in seen_folders:

                        # save the output for each function
                        cookies = find_cookie(target_path, word, target_folder)
                        system = find_sys_info(target_path)
                        credentials = find_credentials(target_path, word)

                        # check for positive output only
                        nf = "404 not found"
                        if system and cookies and credentials:
                            if (nf not in system) and (nf not in cookies) and (('USER' in credentials) and ('PASS' in credentials)): 
                                print(f"\n{Fore.GREEN}------FOLDER{Style.RESET_ALL}: {target_folder}")
                                print((system) + '\n' + (cookies) + '\n' + (credentials))
                                seen_folders.add(target_path)
        print('\n' + "======================================================" + '\n')
    if input("[?] delete cookies (y): ") == "y":
        try:
            shutil.rmtree('main_cookies')
            print(f'[V] cookies successfully deleted')
        except FileNotFoundError as error:
            pass

# ------- search functions

def grab_crypto(path):
    print(Fore.RED, '[ CRYPTO ]', Style.RESET_ALL)
    with open('websites/crypto.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)
    
def grab_eCommerce(path):
    print(Fore.RED, '[ E-COMMERCE ]', Style.RESET_ALL)
    with open('websites/eCommerces.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_emails(path):
    print(Fore.RED, '[ E-MAILS ]', Style.RESET_ALL)
    with open('websites/emails.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)
    
def grab_gaming(path):
    print(Fore.RED, '[ GAMING ]', Style.RESET_ALL)
    with open('websites/gaming.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_giftcards(path):
    print(Fore.RED, '[ GIFT-CARDS ]', Style.RESET_ALL)
    with open('websites/giftcards.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_learning(path):
    print(Fore.RED, '[ LEARNING ]', Style.RESET_ALL)
    with open('websites/learning.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_payments(path):
    print(Fore.RED, '[ PAYMENTS ]', Style.RESET_ALL)
    with open('websites/payments.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_rides(path):
    print(Fore.RED, '[ RIDES AND DELIVERY ]', Style.RESET_ALL)
    with open('websites/rides.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_subscriptions(path):
    print(Fore.RED, '[ SUBSCRIPTIONS ]', Style.RESET_ALL)
    with open('websites/subscriptions.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_travel(path):
    print(Fore.RED, '[ TRAVEL ]', Style.RESET_ALL)
    with open('websites/travel.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_utility(path):
    print(Fore.RED, '[ UTILITY ]', Style.RESET_ALL)
    with open('websites/utility.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_bett(path):
    print(Fore.RED, '[ BETTING ]', Style.RESET_ALL)
    with open('websites/betting.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_passMan(path):
    print(Fore.RED, '[ PSWD MANAGER ]', Style.RESET_ALL)
    with open('websites/passManager.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_porn(path):
    print(Fore.RED, '[ PORN ]', Style.RESET_ALL)
    with open('websites/porn.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_tickets(path):
    print(Fore.RED, '[ TIKETS ]', Style.RESET_ALL)
    with open('websites/tickets.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_cloud(path):
    print(Fore.RED, '[ CLOUD ]', Style.RESET_ALL)
    with open('websites/cloud.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_socials(path):
    print(Fore.RED, '[ SOCIAL MEDIAS ]', Style.RESET_ALL)
    with open('websites/socials.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_wordlist(path):
    print(Fore.RED, '[ JUICY WORDLIST ]', Style.RESET_ALL)
    with open('websites/wordlist.txt', 'r') as f:
        words = f.readlines()
    automate(words, path)

def grab_specific(path):
    seen_folders = set()
    match_counts = defaultdict(int)
    print('[ SPECIFIC ]')
    word = input('[?] Insert the word to look for: ')
    print(f'[!] Word looking for: {word}')
    command = f"grep -r '{word}' {path} | grep -n --color=auto 'sswords.txt'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    for line in result.stdout.splitlines():
        parts = line.split(':', 2)      # will be done at most 2 splits -> [part1, part2, part3]
        if len(parts) >= 2:
            full_path = parts[1] if parts[0].isdigit() else parts[0]
            full_path = full_path.strip()
            # print(full_path)
            if "all password" in full_path.lower():
                full_dir = os.path.dirname(full_path)   # get only the file's directory  
                parts = full_dir.split("/")
                while parts and 'target' not in parts[-1]:
                    parts.pop()
                if not parts:
                    continue
                target_path = os.path.join(*parts)
                target_folder = parts[-1]
                if target_path not in seen_folders:

                    # save the output for each function
                    cookies = find_cookie(target_path, word, target_folder)
                    system = find_sys_info(target_path)
                    credentials = find_credentials(target_path, word)

                    print(f"{Fore.GREEN}------FOLDER{Style.RESET_ALL}: {target_folder}")
                    find_sys_info(target_path)
                    find_cookie(target_path, word, target_folder)
                    find_credentials(target_path, word)
                    seen_folders.add(target_path)
                    print()
                    print()

def grab_all(path):
    grab_crypto(path)
    grab_eCommerce(path)
    grab_emails(path)
    grab_gaming(path)
    grab_giftcards(path)
    grab_learning(path)
    grab_payments(path)
    grab_rides(path)
    grab_subscriptions(path)
    grab_travel(path)
    grab_utility(path)
    grab_bett(path)
    grab_passMan(path)
    grab_porn(path)
    grab_tickets(path)
    grab_cloud(path)
    grab_wordlist(path)

# ---------
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_banner = pyfiglet.figlet_format("logSniper")
    version = 1.0
    print(ascii_banner)
    print(f'[#] log parsing toolkit | v_{version}')

    parser = argparse.ArgumentParser(description='[!] Search for a word in the folder provided')
    parser.add_argument('-p', '--path', type=str, required=True, help="Folder path to search in.")
    args = parser.parse_args()

    if os.path.isdir(args.path):
        uSelection = input("""

[?] Look for:
    
    [0]     crypto
    [1]     eCommerce
    [2]     email providers
    [3]     gaming wSites
    [4]     gift-cards wSites
    [5]     learning platforms
    [6]     banks
    [7]     rides and delivery
    [8]     subscription based wSites
    [9]     travel wSites
    [10]    utlity wSites
    [11]    betting wSites
    [12]    password managers
    [13]    porn wSites
    [14]    tickets wSties
    [15]    juicy wordlist
    [16]    cloud sites
    [17]    social medias
    [18]    specific word
    [333]   complete lookup

    [!] Select what to focus on: """)
        print()

        if int(uSelection) == 0:
            grab_crypto(args.path)
        elif int(uSelection) == 1:
            grab_eCommerce(args.path)
        elif int(uSelection) == 2:
            grab_emails(args.path)
        elif int(uSelection) == 3:
            grab_gaming(args.path)
        elif int(uSelection) == 4:
            grab_giftcards(args.path)
        elif int(uSelection) == 5:
            grab_learning(args.path)
        elif int(uSelection) == 6:
            grab_payments(args.path)
        elif int(uSelection) == 7:
            grab_rides(args.path)
        elif int(uSelection) == 8:
            grab_subscriptions(args.path)
        elif int(uSelection) == 9:
            grab_travel(args.path)
        elif int(uSelection) == 10:
            grab_utility(args.path)
        elif int(uSelection) == 11:
            grab_bett(args.path)
        elif int(uSelection) == 12:
            grab_passMan(args.path)
        elif int(uSelection) == 13:
            grab_porn(args.path)
        elif int(uSelection) == 14:
            grab_tickets(args.path)
        elif int(uSelection) == 15:
            grab_wordlist(args.path)
        elif int(uSelection) == 16:
            grab_cloud(args.path)
        elif int(uSelection) == 17:
            grab_socials(args.path)
        elif int(uSelection) == 18:
            grab_specific(args.path)
        elif int(uSelection) == 333:
            grab_all(args.path)
        else:
            print('[!] Select a valid option')
    else:
        print(f"[!] Error: {args.path} is not a valid directory.")
# ---------

if __name__ == "__main__":
    main()