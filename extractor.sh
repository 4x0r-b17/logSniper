#!/bin/bash
# extractor.sh | script that automate the extraction and renaming steps

# pre-defined main path | define here the main destination
EXTRACT_BASE="./default"

read -p "[+] Enter the path to the archive (.rar or .zip): " ARCHIVE_PATH
read -p "[+] Enter the pack name: " PACK_NAME
read -p "[+] Enter password (leave empty if none): " PASSWORD

# final destination for ectraction
EXTRACT_PATH="${EXTRACT_BASE%/}/$PACK_NAME"

# main folder creation
mkdir -p "$EXTRACT_PATH"
echo ""

# check if file exists
if [[ -f "$ARCHIVE_PATH" ]]; then

    # check extention
    EXT="${ARCHIVE_PATH##*.}"
    EXT_LOWER=$(echo "$EXT" | tr '[:upper:]' '[:lower:]')

    # extraction
    echo "[!] extracting..."
    case "$EXT_LOWER" in
        rar)
            if [[ -z "$PASSWORD" ]]; then
                unrar x -inul "$ARCHIVE_PATH" "$EXTRACT_PATH" > /dev/null
            else
                # password protected
                unrar x -inul "$ARCHIVE_PATH" "$EXTRACT_PATH" -p"$PASSWORD" > /dev/null
            fi
            ;;
        zip)
            if [[ -z "$PASSWORD" ]]; then
                unzip -q -d "$EXTRACT_PATH" "$ARCHIVE_PATH" > /dev/null
            else
                # password protected
                unzip -q -P "$PASSWORD" -d "$EXTRACT_PATH" "$ARCHIVE_PATH" > /dev/null
            fi
            ;;
        *)
            echo "[X] unsupported file type: .$EXT"
            exit 1
            ;;
    esac
    echo "[V] extraction completed to: $EXTRACT_PATH"

    # archive remotion | comment if you want to keep the compressed folder
    echo "[!] removing original archive..."
    rm -rf "$ARCHIVE_PATH"
    echo "[V] archive removed"

    # determine the path to rename
    mapfile -d '' -t subfolders < <(find "$EXTRACT_PATH" -mindepth 1 -maxdepth 1 -type d -print0)

    # check number of sub-folders
    if [[ ${#subfolders[@]} -eq 1 ]]; then
        TARGET_PATH="${subfolders[0]}"      
    else
        TARGET_PATH="$EXTRACT_PATH"
    fi
    
    # rename sub-folders 
    echo "[!] renaming sub-folders..."
    python3 rename.py -p "$TARGET_PATH"

else
    echo "[X] Error: File not found or invalid path"
fi