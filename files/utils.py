from pathlib import Path

def get_file_extention(file_path):
    return Path(file_path).suffix[1:].lower()