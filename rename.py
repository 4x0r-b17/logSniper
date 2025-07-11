# rename.py | this script rename all sub-folders in a main folder allowing a better processing of the target folder path

import os
import argparse

def print_progress(iteration, total, lenght=100):
    percent = iteration/total
    filled_lenght = int(lenght * percent)
    bar = '#' * filled_lenght + ' ' * (lenght - filled_lenght)
    print(f'\rProgress: [{bar}] {iteration}/{total}', end='', flush=True)

def rename(base_path):
    folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]
    total = len(folders)
    for i, folder in enumerate(sorted(folders), start=1):
        old_path = os.path.join(base_path, folder)
        new_folder = f"{i}_target"
        new_path = os.path.join(base_path, new_folder)
        os.rename(old_path, new_path)
        print_progress(i, total)
    print('\n[✅] all done')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str, required=True, help="Folder path to search in.")
    args = parser.parse_args()
    rename(args.path)

if __name__ == "__main__":
    main()