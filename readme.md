# logSniper

logSniper is a modular parsing toolkit designed for Red Team operators, malware analysts, and threat researchers. It automates the extraction of credentials, cookies, and host metadata from browser log dumps or stealer output. The tool supports categorization based on wordlists tied to specific services (e.g., crypto, cloud, bank, gaming...).

---

## Features

- bash-based archive extractor and folder normalizer for bulk operations
- extracts credentials (USER:PASSWORD) from known password dump formats
- finds cookies matching target keywords (e.g., domain names, service names)
- pulls host system information (country, language, timezone, OS version, hostname)
- filters and outputs only valid and complete matches
- wordlist-driven categorization per vertical
---

## Project Structure

```
.
├── Logs&Cookies.py       # main interface
├── credentials.py        # extracts credentials from password files
├── cookies.py            # searches for cookies associated to a specific target and service
├── system.py             # parses system fingerprint (locale, hostname, etc.)
├── rename.py             # renames folders to N_target pattern
├── extractor.sh          # raw archive extraction and auto-renaming
├── requirements.txt
└── websites/             # wordlists per platform/service type
    ├── crypto.txt
    ├── emails.txt
    ├── gaming.txt
    ├── cloud.txt
    └── ...
```

---

## Installation

python 3.8 and following tools are required:
- 'grep', 'unzip', 'unrar'

#### tools intallation
```bash
sudo apt-get update && sudo apt-get install grep unzip unrar -y
```

#### python dependencies installation
```bash
pip install -r requirements.txt
```

---

## Usage

### 1 - archive extraction

use the provided Bash script to extract `.zip` or `.rar` logs into a normalized folder:

```bash
chmod +x extractor.sh
./extractor.sh
```
this will:
- extract the archive to `./default/<PACK_NAME>/`
- Rename subfolders to `1_target`, `2_target`, ... `N_target`.

### 2 - run parser

```bash
python3 Logs&Cookies.py -p ./default/<PACK_NAME>
```

N.B. the script require some minutes to firstly scan the entire archive, for the first scan

### 3 - select a category:

```
[0]  crypto             [10] utility
[1]  eCommerce          [11] betting
[2]  email providers    [12] password managers
[3]  gaming             [13] porn
[4]  giftcards          [14] tickets
[5]  learning           [15] juicy wordlist
[6]  banks/payments     [16] cloud
[7]  rides & delivery   [17] social media
[8]  subscriptions      [18] specific word
[9]  travel             [333] all categories
```
### 4 - output

If valid credentials, cookies, and system info are all present in a folder:

- the match is printed to screen
- cookie dumps are stored in:
  ```
  ./main_cookies/<keyword>/<target_folder>.txt
  ```

Example match output:

```
------FOLDER: 2_target
system info: DE | de-DE | UTC+1 | Windows 10 | DESKTOP-ABC123
cookies: 14 matches
credentials: admin@mail.com | sTr0ngP@ssw0rd
```

---

## Notes

- this tool is designed to run on linux-based systems and relies on standard Unix utilities
- matching logic requires all three components: system info, cookie match, and valid credentials (`USER`, `PASS`); this ensure only complete outputs
- works best on logs structured with stealer-style output (e.g., "All Passwords.txt", "System.txt", cookie strings)

---

## Legal

This tool is intended for **authorized security testing, threat emulation, and malware analysis**. Usage on unauthorized data or systems is prohibited and may be illegal in your jurisdiction